from base.statuses import Status
from tasks.model import Task
from tasks.worker import Worker


def task_runner(browser):
    task = Task()

    for task in task.get_next():
        task.set_status(Status.IN_PROGRESS)

        worker = Worker(browser)
        worker.add_task(task)
        status = worker.run()

        task.set_status(status)
