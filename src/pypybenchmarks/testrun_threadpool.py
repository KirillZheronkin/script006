import time
from multiprocessing.dummy import Pool
from multiprocessing import cpu_count
from hardtask import hard





def main():
    CPUCOUNT = cpu_count()
    inputted = [2 for x in range(100)][:CPUCOUNT]
    pool = Pool(CPUCOUNT)
    result = pool.map(hard,inputted)
    return result


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)

"""
python3.7 testrun_threadpool.py 
11.175792932510376

pypy testrun_threadpool.py 
0.8019084930419922

"""