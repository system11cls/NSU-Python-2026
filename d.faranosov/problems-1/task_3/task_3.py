from sys import argv, stderr
import time
import tracemalloc
from webbrowser import Error

from bitarray import bitarray

start_time = 0
end_time = 0
cur_mem = 0
peak_mem = 0


def get_N(N_str):
    number = int(N_str)
    check_N(number)
    return number

def check_N(N: int):
    if N < 2:
        print(f'Invalid N value - {N}', file=stderr)
        exit(1)

def get_cur_time():
    return time.time()

def start_work():
    global start_time
    start_time = get_cur_time()
    tracemalloc.start()


def end_work():
    global cur_mem, peak_mem, end_time
    cur_mem, peak_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.clear_traces()
    end_time = get_cur_time()

def list_work(N):
    temp_list = [True] * (N + 1)
    temp_list[0] = temp_list[1] = False

    for i in range(N//2):
        if temp_list[i]:
            next_i = i * i
            while next_i < N:
                temp_list[next_i] = False
                next_i += i

    res = []
    for i in range(N):
        if temp_list[i]:
            res.append(i)

    return res



def set_work(N):
    not_prime = set()
    primes = []
    for i in range(2, N):
        if i in not_prime:
            continue
        primes.append(i)
        for j in range(i * i, N, i):
            not_prime.add(j)

    return primes

def bitarray_work(N):
    arr = bitarray(N)
    arr.setall(1)
    arr[0:2] = 0
    for i in range(2, N//2):
        next_i = i * i
        while next_i < N:
            arr[next_i] = 0
            next_i += i

    res = []
    for i, val in enumerate(arr):
        if val == 1:
            res.append(i)

    return res

def Eratosthenes_Sieve(N: int):
    funcs = {'list': list_work,
             'set': set_work,
             'bitarray': bitarray_work}
    for key, func in funcs.items():
        start_work()
        res = func(N)
        end_work()
        time_spent = end_time - start_time

        print(f'{key}: time = {time_spent}, memory in the end = {cur_mem}, memory peak = {peak_mem}\n{res[:100]}\n\n')

if len(argv) < 2:
    print("No max number", file=stderr)
    exit(1)

try:
    N = get_N(argv[1])
    Eratosthenes_Sieve(N)
except ValueError:
    print(f'{argv[1]} is not an integer', file=stderr)
    exit(1)
