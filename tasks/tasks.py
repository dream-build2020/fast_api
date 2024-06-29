import logging
from core.CeleryCore import celery_app
# from utils.config import settings


LOGGER = logging.getLogger(__name__)


class Tasks(object):
    @staticmethod
    @celery_app.tasks
    def sum_add(a: int, b: int) -> int:
        result = a + b
        return result


if __name__ == '__main__':
    pass
