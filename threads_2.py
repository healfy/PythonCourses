from threading import Thread
from time import sleep


class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, name, max_int):
        """Инициализация потока"""
        super(MyThread, self).__init__()
        self.name = name
#         self.max_int = max_int

#     def run(self):
#         """Запуск потока"""
#         for i in range(self.max_int):
#             print('{}: {}'.format(self.name, i))
#             sleep(0.5)


def create_threads():
    """
    Создаем группу потоков
    """
    for i in range(3):
        my_thread = MyThread('Поток {}'.format(i + 1), 10 * (i + 1))
        my_thread.start()


if __name__ == "__main__":
    create_threads()
