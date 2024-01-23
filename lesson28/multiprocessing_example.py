from multiprocessing import Process, Queue, Pool, Lock
import time

def f(x):
    print(f'hello, {x}')

def other_func(q):
    q.put([1, 'a', None])

def fx(x):
    return x*x

def function_to_test_lock(lock, x):
    lock.acquire()
    try:
        print(f'hello {x}')
    finally:
        lock.release()

if __name__ == '__main__':
    '''proc = Process(target=f, args=('Anna',))
    proc.start()
    proc.join()
    q = Queue()
    p = Process(target=other_func, args=(q,))
    p.start()
    print(q.get())
    p.join()
    with Pool(3) as pool:
        print(pool.map(fx, [1,2,3]))'''
    lock = Lock()
    for number in range(20):
        process = Process(target=function_to_test_lock, args=(lock, number))
        process.start()



