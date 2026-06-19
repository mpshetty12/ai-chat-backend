import os

class Settings:
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./chat.db"
    )

    JWT_SECRET = os.getenv("JWI_SECRET", "supersecret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60*24

    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

settings = Settings();