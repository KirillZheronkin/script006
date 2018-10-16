from threading import Lock, Thread


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
    lock = Lock()
    g = 0
    threads = []
    for func in [add_one, add_two]:
        threads.append(Thread(target=func, args=(lock,)))
        threads[-1].start()

    [t.join() for t in threads]
    print(g)