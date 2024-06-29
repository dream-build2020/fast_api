import logging
from tasks.tasks import Tasks

LOGGER = logging.getLogger(__name__)


class Schedule(object):
    @staticmethod
    def schedule_task1():
        Tasks.add.apply_async(args=[2, 3])


if __name__ == '__main__':
    pass
