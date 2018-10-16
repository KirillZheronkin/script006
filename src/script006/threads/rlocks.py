import threading

if __name__ == '__main__':
    num = 0


    rlock = threading.RLock()
    with rlock:
        print("we r inside with rlock")
        rlock.acquire()
        print("trying to re-acquire lock")
        num += 1
        num += 2
        rlock.release()


    lock = threading.Lock()
    with lock:
        print("we r inside with lock")

        lock.acquire()
        print("trying to re-acquire lock")
        num += 1
        num += 2

    print(num)