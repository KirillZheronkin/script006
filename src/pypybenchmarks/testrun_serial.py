from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
import time
from hardtask import hard


def main():
    CPUCOUNT = cpu_count()
    while CPUCOUNT:
        hard()
        CPUCOUNT-=1


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)


"""
python3.7 testrun_serial.py 
8.39017629623413

 pypy --jit off testrun_serial.py 
23.42897129058838

pypy testrun_serial.py 
0.20752382278442383



"""
