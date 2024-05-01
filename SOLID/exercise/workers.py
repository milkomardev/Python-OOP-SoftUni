from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...


class Worker(BaseWorker):

    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BaseWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class ClassicWorker(BaseWorker):

    @staticmethod
    def work():
        print("Давам акъл")


class NotBaseWorker:  # Does not inherit BaseWorker

    @staticmethod
    def work():
        print('I can work too')


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f'`worker` must be subclass of {BaseWorker}')

        self.worker = worker

    def manage(self):
        if self.worker:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
classic_worker = ClassicWorker()
not_base_worker = NotBaseWorker()

try:
    manager.set_worker(classic_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support classic worker....")

try:
    manager.set_worker(not_base_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support not base worker....")
