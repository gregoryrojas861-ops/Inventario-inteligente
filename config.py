import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

class Settings:
    APP_ENV = os.getenv("APP_ENV", "development")
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR / 'inventory.db'}")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret")
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"

settings = Settings()
