from __future__ import annotations

import asyncio
import functools
import logging
import time
import uuid
from collections import OrderedDict
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from typing import AsyncGenerator

import aiofiles
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import CREDIT_PER_IMAGE, OUTPUT_DIR, MAX_CONCURRENT_GENERATIONS
from app.database import AsyncSessionLocal
from app.models.db_models import GeneratedImage as DBGeneratedImage, GenerationJob
from app.services import gemini_service, kimi_service
from app.services.image_processing import optimize_for_shopee
from app.templates.registry import SceneTemplate, TemplateRegistry
from app.templates.styles.registry import InjectionLevel, StyleRegistry

logger = logging.getLogger(__name__)

# Task cleanup constants
MAX_TASK_AGE_SECONDS = 3600  # 1 hour
MAX_TASKS = 200

# Color tone coherence prefix — injected into all prompts in a batch to ensure
# a visually unified set of 9 images with consistent color temperature and tone.
COLOR_COHERENCE_PREFIX = (
    "IMPORTANT VISUAL COHERENCE RULES for this product photo set: "
    "Maintain a consistent warm neutral color temperature (around 5500K) across all shots. "
    "Use the same white balance and exposure feel. "
    "Shadows should be soft and slightly warm. "
    "Highlights should be clean without harsh clipping. "
    "The overall color palette should feel cohesive — as if all images were shot in the same session. "
    "Avoid overly saturated or neon colors. "
    "The product's true colors must be accurately represented in every shot. "
    "\n\n"
)


class ImageStatus(str, Enum):
    PENDING = "pending"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class GeneratedImageResult:
    template_id: str
    template_name: str
    status: ImageStatus = ImageStatus.PENDING
    output_path: str | None = None
    error: str | None = None


@dataclass
class GenerationTask:
    task_id: str
    image_path: Path
    product_type: str
    results: list[GeneratedImageResult] = field(default_factory=list)
    status: str = "pending"
    progress: int = 0
    total: int = 0
    style: str | None = None
    created_at: float = field(default_factory=time.time)
    user_id: str | None = None  # Linked user (None for anonymous/legacy)
    shopee_optimize: bool = False  # Apply Shopee image optimization post-generation


# In-memory task storage with ordered insertion for efficient cleanup
_tasks: OrderedDict[str, GenerationTask] = OrderedDict()


def _cleanup_old_tasks():
    """Remove expired tasks and keep total count within limits."""
    now = time.time()
    # Remove tasks older than MAX_TASK_AGE_SECONDS
    expired = [
        tid for tid, t in _tasks.items()
        if now - t.created_at > MAX_TASK_AGE_SECONDS
    ]
    for tid in expired:
        _tasks.pop(tid, None)
    # If still over limit, remove oldest tasks first
    while len(_tasks) > MAX_TASKS:
        _tasks.popitem(last=False)


def create_task(
    image_path: Path,
    product_type: str,
    template_overrides: dict[str, str] | None = None,
    selected_template_ids: list[str] | None = None,
    style: str | None = None,
    user_id: str | None = None,
    shopee_optimize: bool = False,
) -> GenerationTask:
    """Create a generation task for selected (or all) templates."""
    _cleanup_old_tasks()
    task_id = uuid.uuid4().hex[:12]
    templates = TemplateRegistry.get_templates(product_type)

    # Filter templates if specific ones selected
    if selected_template_ids:
        selected_set = set(selected_template_ids)
        filtered = [t for t in templates if t.id in selected_set]
        if filtered:
            templates = filtered
        else:
            # If all provided IDs are invalid, raise error instead of silently
            # falling back to all templates
            raise ValueError(
                f"None of the selected template IDs match: {selected_template_ids}"
            )

    results = []
    for t in templates:
        results.append(GeneratedImageResult(
            template_id=t.id,
            template_name=t.name,
        ))

    task = GenerationTask(
        task_id=task_id,
        image_path=image_path,
        product_type=product_type,
        results=results,
        total=len(results),
        style=style,
        user_id=user_id,
        shopee_optimize=shopee_optimize,
    )
    _tasks[task_id] = task
    return task


async def persist_task_to_db(task: GenerationTask) -> None:
    """Write task and its image placeholders to the database.

    Called after create_task() so that the job is durable. Uses its own
    session to avoid coupling with the request's DB session lifecycle.
    """
    if not task.user_id:
        return  # Anonymous tasks (legacy mode) skip DB persistence

    try:
        async with AsyncSessionLocal() as db:
            job = GenerationJob(
                id=task.task_id,
                user_id=task.user_id,
                status=task.status,
                product_type=task.product_type,
                style=task.style,
                image_path=str(task.image_path),
                total_images=task.total,
                completed_images=0,
                credits_charged=task.total * CREDIT_PER_IMAGE,
            )
            db.add(job)

            for r in task.results:
                db_img = DBGeneratedImage(
                    job_id=task.task_id,
                    template_id=r.template_id,
                    template_name=r.template_name,
                    status=r.status.value,
                )
                db.add(db_img)

            await db.commit()
            logger.info(f"Persisted task {task.task_id} to DB ({task.total} images)")
    except Exception as e:
        logger.error(f"Failed to persist task {task.task_id} to DB: {e}")


async def _update_image_status_db(
    task_id: str,
    template_id: str,
    status: str,
    output_path: str | None = None,
    error: str | None = None,
) -> None:
    """Update a single generated_image row in the database."""
    try:
        async with AsyncSessionLocal() as db:
            await db.execute(
                update(DBGeneratedImage)
                .where(
                    DBGeneratedImage.job_id == task_id,
                    DBGeneratedImage.template_id == template_id,
                )
                .values(
                    status=status,
                    output_path=output_path,
                    error=error,
                )
            )
            await db.commit()
    except Exception as e:
        logger.error(f"Failed to update image status in DB ({task_id}/{template_id}): {e}")


async def _update_job_status_db(
    task_id: str,
    status: str,
    completed_images: int | None = None,
    error_message: str | None = None,
) -> None:
    """Update a generation_job row in the database."""
    try:
        async with AsyncSessionLocal() as db:
            values: dict = {"status": status}
            if completed_images is not None:
                values["completed_images"] = completed_images
            if error_message is not None:
                values["error_message"] = error_message

            await db.execute(
                update(GenerationJob)
                .where(GenerationJob.id == task_id)
                .values(**values)
            )
            await db.commit()
    except Exception as e:
        logger.error(f"Failed to update job status in DB ({task_id}): {e}")


def get_task(task_id: str) -> GenerationTask | None:
    return _tasks.get(task_id)


async def get_task_from_db(task_id: str) -> GenerationTask | None:
    """Fallback: load a task from DB when not in memory cache.

    This supports page-refresh recovery — the frontend can re-fetch results
    for a task_id that was evicted from memory but persists in the DB.
    """
    try:
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(GenerationJob).where(GenerationJob.id == task_id)
            )
            job = result.scalar_one_or_none()
            if not job:
                return None

            # Load associated images
            img_result = await db.execute(
                select(DBGeneratedImage).where(DBGeneratedImage.job_id == task_id)
            )
            db_images = list(img_result.scalars().all())

            results = []
            for img in db_images:
                results.append(GeneratedImageResult(
                    template_id=img.template_id,
                    template_name=img.template_name,
                    status=ImageStatus(img.status) if img.status in ImageStatus.__members__.values() else ImageStatus.PENDING,
                    output_path=img.output_path,
                    error=img.error,
                ))

            task = GenerationTask(
                task_id=task_id,
                image_path=Path(job.image_path),
                product_type=job.product_type,
                results=results,
                status=job.status,
                progress=job.completed_images,
                total=job.total_images,
                style=job.style,
                user_id=job.user_id,
            )

            # Re-populate memory cache so subsequent in-flight lookups are fast
            _tasks[task_id] = task
            return task

    except Exception as e:
        logger.error(f"Failed to load task {task_id} from DB: {e}")
        return None


async def recover_stale_tasks() -> int:
    """Mark stale running/pending jobs as failed on startup.

    Called once during application startup to clean up any jobs that were
    interrupted by a crash or restart. Returns the count of recovered tasks.
    """
    try:
        async with AsyncSessionLocal() as db:
            result = await db.execute(
                select(GenerationJob).where(
                    GenerationJob.status.in_(["pending", "running", "starting"])
                )
            )
            stale_jobs = list(result.scalars().all())
            count = 0

            for job in stale_jobs:
                new_status = "partial" if job.completed_images > 0 else "failed"
                await db.execute(
                    update(GenerationJob)
                    .where(GenerationJob.id == job.id)
                    .values(
                        status=new_status,
                        error_message="伺服器重啟，任務被中斷",
                    )
                )

                # Mark any non-completed images as failed
                await db.execute(
                    update(DBGeneratedImage)
                    .where(
                        DBGeneratedImage.job_id == job.id,
                        DBGeneratedImage.status.in_(["pending", "generating"]),
                    )
                    .values(
                        status="failed",
                        error="伺服器重啟，生成被中斷",
                    )
                )
                count += 1

            await db.commit()
            if count > 0:
                logger.info(f"Recovered {count} stale tasks on startup")
            return count

    except Exception as e:
        logger.error(f"Failed to recover stale tasks: {e}")
        return 0


def _build_results_payload(task_id: str, results: list[GeneratedImageResult]) -> list[dict]:
    return [
        {
            "template_id": r.template_id,
            "template_name": r.template_name,
            "status": r.status.value,
            "url": f"/api/outputs/{task_id}/{r.template_id}.png" if r.output_path else None,
            "error": r.error,
        }
        for r in results
    ]


async def run_generation(
    task_id: str,
    template_overrides: dict[str, str] | None = None,
) -> AsyncGenerator[dict, None]:
    """Run image generation for all templates, yielding progress events."""
    task = _tasks.get(task_id)
    if not task:
        yield {"event": "error", "data": "Task not found"}
        return

    task.status = "running"
    # Update DB status
    await _update_job_status_db(task_id, "running")

    # Only use templates that match this task's results (supports selective generation)
    all_templates = TemplateRegistry.get_templates(task.product_type)
    result_ids = {r.template_id for r in task.results}
    templates = [t for t in all_templates if t.id in result_ids]
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_GENERATIONS)

    task_output_dir = OUTPUT_DIR / task_id
    task_output_dir.mkdir(parents=True, exist_ok=True)

    # Pre-load product image bytes once — avoids repeated disk reads for every
    # generation call within the batch (9 reads → 1 read).
    # Use aiofiles to avoid blocking the event loop on disk I/O.
    async with aiofiles.open(task.image_path, "rb") as f:
        product_image_bytes = await f.read()
    logger.info(f"Pre-loaded product image ({len(product_image_bytes)} bytes) for batch generation")

    # Use an Event to signal when any single image finishes
    progress_event = asyncio.Event()

    async def generate_single(index: int, template: SceneTemplate):
        async with semaphore:
            result = task.results[index]
            result.status = ImageStatus.GENERATING
            # Update DB: generating
            await _update_image_status_db(task_id, template.id, "generating")
            # Signal so SSE can push "generating" status
            progress_event.set()

            # Use custom prompt if provided, otherwise apply style injection
            if template_overrides and template.id in template_overrides:
                prompt = template_overrides[template.id]
            else:
                # Apply style modifier based on template's injection_level
                injection_level = InjectionLevel(template.injection_level)
                prompt = StyleRegistry.assemble_prompt(
                    base_prompt=template.prompt,
                    style_id=task.style,
                    injection_level=injection_level,
                )

            # Inject color coherence prefix for batch visual harmony
            prompt = COLOR_COHERENCE_PREFIX + prompt
            logger.info(f"Prompt for {template.id} (style={task.style}, level={template.injection_level}): {prompt[:120]}...")

            try:
                provider = template.recommended_provider
                if provider == "kimi":
                    image_bytes = await kimi_service.generate_scene_image(
                        product_image_path=task.image_path,
                        prompt=prompt,
                    )
                else:
                    image_bytes = await gemini_service.generate_scene_image_from_bytes(
                        image_bytes=product_image_bytes,
                        prompt=prompt,
                        aspect_ratio=template.aspect_ratio,
                    )

                output_filename = f"{template.id}.png"
                output_path = task_output_dir / output_filename
                async with aiofiles.open(output_path, "wb") as f:
                    await f.write(image_bytes)

                # Apply Shopee optimization if requested
                if task.shopee_optimize:
                    loop = asyncio.get_running_loop()
                    optimized = await loop.run_in_executor(
                        None, optimize_for_shopee, str(output_path),
                    )
                    output_path = Path(optimized)

                result.status = ImageStatus.COMPLETED
                result.output_path = str(output_path)
                logger.info(f"Generated {template.id} successfully")
                # Update DB: completed
                await _update_image_status_db(
                    task_id, template.id, "completed",
                    output_path=str(output_path),
                )

            except Exception as e:
                logger.error(f"Failed to generate {template.id}: {e}")
                # Retry once — use the same provider as initial attempt
                try:
                    if provider == "kimi":
                        image_bytes = await kimi_service.generate_scene_image(
                            product_image_path=task.image_path,
                            prompt=prompt,
                        )
                    else:
                        image_bytes = await gemini_service.generate_scene_image_from_bytes(
                            image_bytes=product_image_bytes,
                            prompt=prompt,
                            aspect_ratio=template.aspect_ratio,
                        )
                    output_filename = f"{template.id}.png"
                    output_path = task_output_dir / output_filename
                    async with aiofiles.open(output_path, "wb") as f:
                        await f.write(image_bytes)

                    # Apply Shopee optimization if requested
                    if task.shopee_optimize:
                        loop = asyncio.get_running_loop()
                        optimized = await loop.run_in_executor(
                            None, optimize_for_shopee, str(output_path),
                        )
                        output_path = Path(optimized)

                    result.status = ImageStatus.COMPLETED
                    result.output_path = str(output_path)
                    logger.info(f"Generated {template.id} on retry")
                    # Update DB: completed (retry)
                    await _update_image_status_db(
                        task_id, template.id, "completed",
                        output_path=str(output_path),
                    )
                except Exception as retry_err:
                    result.status = ImageStatus.FAILED
                    result.error = str(retry_err)
                    logger.error(f"Retry also failed for {template.id}: {retry_err}")
                    # Update DB: failed
                    await _update_image_status_db(
                        task_id, template.id, "failed",
                        error=str(retry_err),
                    )

            task.progress += 1
            # Update DB: job progress
            await _update_job_status_db(task_id, "running", completed_images=task.progress)
            # Signal progress to the SSE loop
            progress_event.set()

    # Launch all tasks
    gen_tasks = []
    for i, template in enumerate(templates):
        gen_tasks.append(asyncio.create_task(generate_single(i, template)))

    # Yield initial started event
    yield {"event": "started", "task_id": task_id, "total": task.total}

    # Yield progress events whenever any image status changes
    last_progress = -1
    while task.progress < task.total:
        # Wait for a status change or timeout (for periodic heartbeat)
        progress_event.clear()
        try:
            await asyncio.wait_for(progress_event.wait(), timeout=2.0)
        except asyncio.TimeoutError:
            pass

        # Only yield if something actually changed
        if task.progress != last_progress:
            last_progress = task.progress
            yield {
                "event": "progress",
                "task_id": task_id,
                "progress": task.progress,
                "total": task.total,
                "results": _build_results_payload(task_id, task.results),
            }

    # Wait for all to finish (they should be done already)
    await asyncio.gather(*gen_tasks, return_exceptions=True)

    # Determine overall status
    completed_count = sum(1 for r in task.results if r.status == ImageStatus.COMPLETED)
    if completed_count == task.total:
        task.status = "completed"
    elif completed_count > 0:
        task.status = "partial"
    else:
        task.status = "failed"

    # Final DB update
    await _update_job_status_db(task_id, task.status, completed_images=completed_count)

    yield {
        "event": "completed",
        "task_id": task_id,
        "status": task.status,
        "progress": task.total,
        "total": task.total,
        "results": _build_results_payload(task_id, task.results),
    }


async def regenerate_single(
    task_id: str,
    template_id: str,
    custom_prompt: str | None = None,
) -> GeneratedImageResult:
    """Regenerate a single image within an existing task."""
    task = _tasks.get(task_id)
    if not task:
        raise RuntimeError("Task not found")

    # Find the result entry
    result = None
    for r in task.results:
        if r.template_id == template_id:
            result = r
            break
    if not result:
        raise RuntimeError(f"Template {template_id} not found in task")

    # Find the template
    all_templates = TemplateRegistry.get_templates(task.product_type)
    template = None
    for t in all_templates:
        if t.id == template_id:
            template = t
            break
    if not template:
        raise RuntimeError(f"Template {template_id} not registered")

    result.status = ImageStatus.GENERATING
    result.error = None
    await _update_image_status_db(task_id, template_id, "generating")

    if custom_prompt:
        prompt = custom_prompt
    else:
        # Apply style injection for regeneration too
        injection_level = InjectionLevel(template.injection_level)
        prompt = StyleRegistry.assemble_prompt(
            base_prompt=template.prompt,
            style_id=task.style,
            injection_level=injection_level,
        )

    # Inject color coherence prefix for visual harmony
    prompt = COLOR_COHERENCE_PREFIX + prompt
    task_output_dir = OUTPUT_DIR / task_id

    try:
        image_bytes = await gemini_service.generate_scene_image(
            product_image_path=task.image_path,
            prompt=prompt,
            aspect_ratio=template.aspect_ratio,
        )
        output_path = task_output_dir / f"{template_id}.png"
        async with aiofiles.open(output_path, "wb") as f:
            await f.write(image_bytes)
        result.status = ImageStatus.COMPLETED
        result.output_path = str(output_path)
        logger.info(f"Regenerated {template_id} successfully")
        await _update_image_status_db(
            task_id, template_id, "completed",
            output_path=str(output_path),
        )
    except Exception as e:
        result.status = ImageStatus.FAILED
        result.error = str(e)
        logger.error(f"Regeneration failed for {template_id}: {e}")
        await _update_image_status_db(
            task_id, template_id, "failed",
            error=str(e),
        )

    return result


async def generate_variants(
    task_id: str,
    template_id: str,
    count: int = 4,
) -> list[dict]:
    """Generate multiple variants for a single template.

    Each variant uses the same prompt but the inherent randomness in image
    generation produces different visual results. Returns a list of
    {variant_index, url} dicts.
    """
    task = _tasks.get(task_id)
    if not task:
        raise RuntimeError("Task not found")

    # Find the template
    all_templates = TemplateRegistry.get_templates(task.product_type)
    template = None
    for t in all_templates:
        if t.id == template_id:
            template = t
            break
    if not template:
        raise RuntimeError(f"Template {template_id} not registered")

    # Build prompt (same as normal generation)
    injection_level = InjectionLevel(template.injection_level)
    prompt = StyleRegistry.assemble_prompt(
        base_prompt=template.prompt,
        style_id=task.style,
        injection_level=injection_level,
    )
    prompt = COLOR_COHERENCE_PREFIX + prompt

    task_output_dir = OUTPUT_DIR / task_id
    task_output_dir.mkdir(parents=True, exist_ok=True)

    # Pre-load product image once (non-blocking)
    async with aiofiles.open(task.image_path, "rb") as f:
        product_image_bytes = await f.read()

    # Generate variants concurrently (max 4 at once)
    semaphore = asyncio.Semaphore(count)
    variants: list[dict] = []

    async def gen_one(idx: int):
        async with semaphore:
            try:
                image_bytes = await gemini_service.generate_scene_image_from_bytes(
                    image_bytes=product_image_bytes,
                    prompt=prompt,
                    aspect_ratio=template.aspect_ratio,
                )
                filename = f"{template_id}_v{idx}.png"
                output_path = task_output_dir / filename
                async with aiofiles.open(output_path, "wb") as f:
                    await f.write(image_bytes)
                variants.append({
                    "variant_index": idx,
                    "url": f"/api/outputs/{task_id}/{filename}",
                })
                logger.info(f"Variant {idx} for {template_id} generated successfully")
            except Exception as e:
                logger.error(f"Variant {idx} for {template_id} failed: {e}")
                variants.append({
                    "variant_index": idx,
                    "url": None,
                    "error": str(e),
                })

    tasks = [asyncio.create_task(gen_one(i)) for i in range(count)]
    await asyncio.gather(*tasks, return_exceptions=True)

    # Sort by index for consistent ordering
    variants.sort(key=lambda v: v["variant_index"])
    return variants


async def select_variant(
    task_id: str,
    template_id: str,
    variant_index: int,
) -> GeneratedImageResult:
    """Replace the main image for a template with the chosen variant."""
    task = _tasks.get(task_id)
    if not task:
        raise RuntimeError("Task not found")

    task_output_dir = OUTPUT_DIR / task_id
    variant_path = task_output_dir / f"{template_id}_v{variant_index}.png"
    main_path = task_output_dir / f"{template_id}.png"

    if not variant_path.exists():
        raise RuntimeError(f"Variant {variant_index} not found for {template_id}")

    # Copy variant to main path (non-blocking)
    loop = asyncio.get_running_loop()
    import shutil
    await loop.run_in_executor(None, functools.partial(shutil.copy2, variant_path, main_path))

    # Update the result entry
    result = None
    for r in task.results:
        if r.template_id == template_id:
            result = r
            break
    if result:
        result.status = ImageStatus.COMPLETED
        result.output_path = str(main_path)
        result.error = None
        # Update DB
        await _update_image_status_db(
            task_id, template_id, "completed",
            output_path=str(main_path),
        )

    logger.info(f"Selected variant {variant_index} for {template_id}")
    return result
