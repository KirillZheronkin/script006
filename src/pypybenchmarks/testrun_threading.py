import time
from multiprocessing import cpu_count
from threading import Thread
from hardtask import hard





def main():
    CPUCOUNT = cpu_count()
    threads = []
    for _ in range(CPUCOUNT):
        t = Thread(target=hard)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)


"""
python3.7 testrun_threading.py 
13.228646039962769

pypy testrun_threading.py 
0.803076982498169


"""
