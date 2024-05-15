from pydantic import BaseConfig


class APISettings(BaseConfig):
    HOST = "127.0.0.1"
    CELERY_BROKER = 'redis://localhost:6379/0'
    TASKS = 10


settings = APISettings()
