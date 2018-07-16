from datetime import datetime
from multiprocessing import Process


def doubler(number):
    print(number ** (10 ** 6))


if __name__ == '__main__':

    start_time = datetime.now()

    procs = []

    for i in range(6, 10):
        proc = Process(target=doubler, args=(i,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()

    end_time = datetime.now()

    print('Duration: {}'.format(end_time - start_time))
