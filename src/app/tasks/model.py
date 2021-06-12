import time
from tasks.processor import Processor
from base.statuses import Status


class Task:
    def __init__(self):
        self.processor = Processor()

    def get_next(self, offset=0):
        while True:
            data = self.processor.get_next_task(offset)

            if not data:
                print('Нет доступных задач')
                offset = 0
                time.sleep(5)
                continue

            for k, v in data.items():
                setattr(self, k, v)

            print(f'Найдена новая задача c {data.get("profile")}')
            yield self
            offset += 1

    def upload_post_data(self, posts):
        for post in posts:
            self.processor.upload_post_data(self.profile, post)

    def set_status(self, status):
        if status == Status.COMPLETED:
            self.done()
        elif status == Status.ERROR:
            self.failed()
        elif status == Status.IN_PROGRESS:
            self.in_progress()

    def done(self):
        self.processor.update_status(Status.COMPLETED, self.profile)

    def in_progress(self):
        self.processor.update_status(Status.IN_PROGRESS, self.profile)

    def failed(self):
        self.processor.update_status(Status.ERROR, self.profile)
