from pydantic import BaseConfig


class APISettings(BaseConfig):
    HOST = "192.168.31.44"
    CELERY_BROKER = 'redis://localhost:6379/0'
    TASKS = 10


settings = APISettings()
