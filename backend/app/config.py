import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
OUTPUT_DIR = BASE_DIR / "outputs"

UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "") or "AIzaSyDBQnuu9lV8JVGGoOuMrtXiqvy-6j_P_Ho"
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY", "")

# CORS origins — comma-separated list, defaults to localhost:3000
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
    if origin.strip()
]

MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
MAX_CONCURRENT_GENERATIONS = 5

# API Key persistence file
API_KEYS_FILE = BASE_DIR / ".api_keys.json"

# --- Database ---
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite+aiosqlite:///{DATA_DIR}/ecom.db")

# --- Auth ---
JWT_SECRET = os.getenv("JWT_SECRET", "")
JWT_ALGORITHM = "HS256"
JWT_EXPIRY_HOURS = 24

# Auto-generate JWT_SECRET on first run if not set
if not JWT_SECRET:
    import secrets
    JWT_SECRET = secrets.token_urlsafe(32)
    # Persist to .env so it survives restarts
    env_path = BASE_DIR / ".env"
    try:
        existing = env_path.read_text() if env_path.exists() else ""
        if "JWT_SECRET" not in existing:
            with open(env_path, "a") as f:
                f.write(f"\nJWT_SECRET={JWT_SECRET}\n")
    except Exception:
        pass  # Best effort

# --- Credits ---
FREE_CREDITS = 50  # Credits for new users
CREDIT_PER_IMAGE = 1  # 1 credit per generated image
