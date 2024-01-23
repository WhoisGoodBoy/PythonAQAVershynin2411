import subprocess
import concurrent.futures
import datetime


'''
print(datetime.datetime.now())
result = subprocess.run(['python', 'threads_1.py'], shell=True, capture_output=True, text=True)
print(result.stdout)
result2 = subprocess.run(['python', 'threads_1.py'], shell=True, capture_output=True, text=True)
print(result2.stdout)
print(datetime.datetime.now())
'''


def threads_subprocess(name):
    print(f'we`re running {name} file rn')
    result = subprocess.run(['python', name], shell=True, capture_output=True, text=True)
    print(result.stdout)
    print(f'we`re finishing with {name} file rn')


with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(threads_subprocess, ['threads_1.py', 'threads_2.py', 'threads_1.py', 'threads_2.py', 'threads_1.py', 'threads_2.py'])
