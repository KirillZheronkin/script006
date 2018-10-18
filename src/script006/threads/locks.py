from threading import Lock, Thread
from time import sleep

@threaded
def function1():
    while True:
        print("im alive")
        sleep(3)


def add_one(lock):
    global g
    lock.acquire()
    g += 1
    lock.release()

def add_two(lock):
    global g
    with lock:
        g += 2



if __name__ == '__main__':
    t = function1()

    # lock = Lock()
    # g = 0
    # threads = []
    # for func in [add_one, add_two]:
    #     t = Thread(target=func, args=(lock,))
    #     # t.is_alive()
    #     threads.append()
    #     threads[-1].start()
    #
    # [t.join() for t in threads]
    # print(g)