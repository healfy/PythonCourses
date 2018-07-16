from datetime import datetime
from multiprocessing import Process
import threading


def linear_count(array):
    result = []
    for number in array:
        result.append(number ** (10**6))
    return result


start_time = datetime.now()

print(linear_count([6, 7, 8, 9]))

end_time = datetime.now()

print('Duration: {}'.format(end_time - start_time))


def procs_count(number):
    print(number ** (10 ** 6))


if __name__ == '__main__':

    start_time = datetime.now()

    procs = []

    for i in range(6, 10):
        proc = Process(target=procs_count, args=(i,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()

    end_time = datetime.now()

    print('Duration: {}'.format(end_time - start_time))


def thread_count(number):
    print(number ** (10**6))


if __name__ == '__main__':

    start_time = datetime.now()

    for i in range(6, 10):
        my_thread = threading.Thread(target=thread_count, args=(i,))
        my_thread.start()
        my_thread.join()

    end_time = datetime.now()

    print('Duration: {}'.format(end_time - start_time))
