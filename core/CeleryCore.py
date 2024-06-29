from celery import Celery
# from utils.config import settings


celery_app = Celery('celery_tasks',
                    broker='redis://localhost:6379/0',
                    include=["tasks.tasks"]
                    )
