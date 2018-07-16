import threading
from datetime import datetime


def counter(number):
    print(number ** (10**6))


if __name__ == '__main__':

    start_time = datetime.now()

    for i in range(6, 10):
        my_thread = threading.Thread(target=counter, args=(i,))
        my_thread.start()
        my_thread.join()

    end_time = datetime.now()

    print('Duration: {}'.format(end_time - start_time))
