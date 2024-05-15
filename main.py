from tasks.tasks import Tasks

if __name__ == '__main__':
    Tasks.sum_add.apply_async(kwargs={'a': 1, 'b': 1})
    pass
