import os

# settings.py
# Configuration settings for the application

class Settings:
    APP_NAME: str = "Address Book Service"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    API_PREFIX: str = os.getenv("API_PREFIX", "/api/v1")

settings = Settings()