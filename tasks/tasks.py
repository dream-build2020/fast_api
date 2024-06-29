import logging
from core.CeleryCore import celery_app

LOGGER = logging.getLogger(__name__)


class Tasks(object):
    @staticmethod
    @celery_app.tasks
    def sum_add(a: int, b: int) -> int:
        result = a + b
        return result


if __name__ == '__main__':
    pass
