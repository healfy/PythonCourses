import random
import threading
from time import sleep



# def writer(x, lock):
#     lock.acquire()
#     for i in range(5):
#         print('Potok {}: {}'.format(x, i))
#         sleep(0.5)
#     lock.release()
# def writer(x):
#     with semaphore:
#         for i in range(5):
#             print('Potok {}: {}'.format(x, i))
#             sleep(random.randint(1, 3))
def writer(x):
    for i in range(5):
        print('Potok {}: {}'.format(x, i))
        sleep(0.25 * x)
    barrier.wait()
    print('Potok {} завершен'.format(x))

#lock = threading.Lock()
barrier = threading.Barrier(3, timeout=10)
# semaphore = threading.Semaphore(2)
t1 = threading.Thread(target=writer, args=(1,))
t2 = threading.Thread(target=writer, args=(2,))
t3 = threading.Thread(target=writer, args=(3,))

# start threads
t1.start()
t2.start()
t3.start()

