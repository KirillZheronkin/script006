import time
from multiprocessing import Pool
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
python3.7 testrun_processpool.py 
4.200903415679932

pypy testrun_processpool.py 
0.37141990661621094


"""
