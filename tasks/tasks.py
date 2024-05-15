import logging
from core.CeleryCore import celery_app

LOGGER = logging.getLogger(__name__)


class Tasks(object):
    @staticmethod
    @celery_app.tasks
    def sum_add(a: int, b: int):
        result = sum(a + b)
        print(result)
        return result
        pass


if __name__ == '__main__':
    pass
