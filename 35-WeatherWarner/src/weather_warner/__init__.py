from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
ROOT_DIR = Path(__file__).resolve().parents[3]

load_dotenv(ROOT_DIR / ".env")
