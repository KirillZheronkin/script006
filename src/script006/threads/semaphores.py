import random, time
from threading import BoundedSemaphore, Thread

"""Implements a bounded semaphore.

A bounded semaphore checks to make sure its current value doesn't exceed its
initial value. If it does, ValueError is raised. In most situations
semaphores are used to guard resources with limited capacity.

If the semaphore is released too many times it's a sign of a bug. If not
given, value defaults to 1.

Like regular semaphores, bounded semaphores manage a counter representing
the number of release() calls minus the number of acquire() calls, plus an
initial value. The acquire() method blocks if necessary until it can return
without making the counter negative. If not given, value defaults to 1.

"""

def producer(container, nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        try:
            container.release()
            print("Produced an item.")
        except ValueError:
            print("Full, skipping.")

def consumer(container, nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2, 5))
        print(time.ctime(), end=": ")
        if container.acquire(False):
            print("Consumed an item.")
        else:
            print("Empty, skipping.")


if __name__ == '__main__':

    LIMIT = 2
    container = BoundedSemaphore(LIMIT)
    threads = []
    nloops = 4
    print("Starting with %s items." % LIMIT)
    threads.append(Thread(target=producer, args=(container, nloops,)))
    threads.append(Thread(target=consumer, args=(container, nloops + 3,)))
    for thread in threads:  # Starts all the threads.
        thread.start()
    for thread in threads:  # Waits for threads to complete before moving on with the main script.
        thread.join()
