from celery import Celery
from utils.config import settings


celery_app = Celery('celery_tasks',
                    broker=settings.CELERY_BROKER,
                    include=["tasks.tasks"]
                    )
