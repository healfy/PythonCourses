import threading
from time import sleep


# def writer(x):
#
#     with lock:
#         for i in range(5):
#             print('Поток {} {}'.format(x, i))
#             sleep(0.25)
def writer(x):

    with semaphore:
        for i in range(5):
            print('Поток {} {}'.format(x, i))
            sleep(0.25)


semaphore = threading.Semaphore(2)
# init threads
t1 = threading.Thread(target=writer, args=(1,))
t2 = threading.Thread(target=writer, args=(2,))
t3 = threading.Thread(target=writer, args=(3,))

# start threads
t1.start()
t2.start()
t3.start()
