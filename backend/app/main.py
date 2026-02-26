import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import CORS_ORIGINS, OUTPUT_DIR, UPLOAD_DIR
from app.routers import (
    analysis,
    atmosphere,
    auth,
    batch,
    credits,
    detail_layout,
    generate,
    history,
    optimization,
    projects,
    scenes,
    settings,
    storyboard,
    themes,
    upload,
)

# Configure logging so app.services.* logs are visible
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s: %(message)s")
logging.getLogger("app").setLevel(logging.INFO)

# Import templates package to trigger registration of all product types
import app.templates  # noqa: F401

app = FastAPI(
    title="E-Commerce Image Generator",
    description="一鍵生成 9 張電商產品圖",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware stack (order matters: first added = outermost)
from app.middleware.error_handler import ErrorHandlerMiddleware
from app.middleware.audit_log import AuditLogMiddleware
from app.middleware.rate_limit import RateLimitMiddleware

app.add_middleware(RateLimitMiddleware)
app.add_middleware(AuditLogMiddleware)
app.add_middleware(ErrorHandlerMiddleware)

# Serve uploaded and generated images
app.mount("/api/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")
app.mount("/api/outputs", StaticFiles(directory=str(OUTPUT_DIR)), name="outputs")

app.include_router(auth.router)
app.include_router(upload.router)
app.include_router(generate.router)
app.include_router(settings.router)
app.include_router(history.router)
app.include_router(credits.router)
app.include_router(batch.router)
app.include_router(projects.router)

# V2 routers
app.include_router(analysis.router)
app.include_router(scenes.router)
app.include_router(storyboard.router)
app.include_router(optimization.router)
app.include_router(detail_layout.router)
app.include_router(atmosphere.router)
app.include_router(themes.router)


@app.on_event("startup")
async def startup():
    """Initialize database and recover stale tasks on startup."""
    from app.database import init_db
    from app.services.generation_service import recover_stale_tasks

    logger = logging.getLogger("app.startup")
    logger.info("Initializing database...")
    await init_db()
    logger.info("Database initialized successfully")

    recovered = await recover_stale_tasks()
    if recovered:
        logger.info(f"Recovered {recovered} stale tasks from previous run")


@app.get("/api/health")
async def health():
    return {"status": "ok"}
