import time
import concurrent.futures



def sleepy_func(name):
    print(f'we`re entering {name} function, congratulations!')
    time.sleep(5)
    print(f'we`re leaving {name} function, good luck')

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(sleepy_func, range(10))
