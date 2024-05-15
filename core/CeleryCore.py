from celery import Celery
from utils.config import settings


celery_app = Celery('tasks',
                    brokerm=settings.CELERY_BROKER,
                    include=["tasks.tasks"],
                    # tasks=settings.TASKS
                    )
pass
