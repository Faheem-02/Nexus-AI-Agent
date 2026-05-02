import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
MAX_STEPS = int(os.getenv("MAX_STEPS", "20"))
RETRY_LIMIT = int(os.getenv("RETRY_LIMIT", "3"))

ENABLE_BROWSER_TOOL = os.getenv("ENABLE_BROWSER_TOOL", "false").lower() in ("1", "true", "yes", "on")
ENABLE_GOOGLE_TOOL = os.getenv("ENABLE_GOOGLE_TOOL", "false").lower() in ("1", "true", "yes", "on")

