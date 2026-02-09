FROM python:3.11-slim

WORKDIR /app

# System dependencies for rembg (OpenCV) and Pillow
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download rembg model so first request isn't slow
RUN python -c "from rembg import remove; from PIL import Image; import io; \
    img = Image.new('RGB', (10, 10), 'white'); \
    buf = io.BytesIO(); img.save(buf, 'PNG'); buf.seek(0); \
    remove(buf.read())" || true

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p uploads outputs data

EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/health')" || exit 1

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
