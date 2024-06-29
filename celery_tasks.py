import logging
from tasks.tasks import Tasks

LOGGER = logging.getLogger(__name__)


class Schedule(object):
    @staticmethod
    def schedule_task1():
        Tasks.sum_add.apply_async(kwargs={'a': 2, 'b': 3})


if __name__ == '__main__':
    pass
