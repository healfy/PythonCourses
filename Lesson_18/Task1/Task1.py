import random
from threading import Thread
from time import sleep
import threading


class CountThread(Thread):

    def __init__(self, name, barrier, semaphore, lock, event):
        super(CountThread, self).__init__()
        self.name = name
        self.barrier = barrier
        self.semaphore = semaphore
        self.lock = lock
        self.event = event

    def run(self):

        print('{}: {}'.format(self.name, 1))
        sleep(random.randint(1, 3))

        self.barrier.wait()

        with self.semaphore:
            print('{}: {}'.format(self.name, 2))
            sleep(random.randint(1, 3))

        with self.lock:
            print('{}: {}'.format(self.name, 3))
            sleep(random.randint(1, 3))

        self.barrier.wait()

        print('{}: {}'.format(self.name, 4))
        sleep(random.randint(1, 3))

        if self.name == 'Поток 1':
            print('{}: {}'.format(self.name, 5))
            sleep(random.randint(1, 3))
            self.event.set()
        else:
            self.event.wait()
            print('{}: {}'.format(self.name, 5))


def create_threads():
    threads = []
    lock = threading.Lock()
    event = threading.Event()
    max_connections = 3
    semaphore = threading.BoundedSemaphore(max_connections)
    barrier = threading.Barrier(3, timeout=10)
    for i in range(6):
        my_thread = CountThread('Поток {}'.format(i + 1), barrier, semaphore,
                                lock, event)
        threads.append(my_thread)
        my_thread.start()
    for thread in threads:
        thread.join()
    print(6)


if __name__ == '__main__':
    create_threads()
