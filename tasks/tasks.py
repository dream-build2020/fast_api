import logging
from celery import Celery
# from utils.config import settings


LOGGER = logging.getLogger(__name__)

celery_app = Celery('tasks',
                    broker='redis://localhost:6379/0',
                    include=["tasks.tasks"]
                    )


class Tasks(object):
    @staticmethod
    @celery_app.tasks
    def sum_add(a: int, b: int) -> int:
        result = a + b
        return result


if __name__ == '__main__':
    pass
