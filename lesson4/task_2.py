# Задание-2: Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.


import timeit
import cProfile

# алгоритм «Решето Эратосфена»


def sieve(n):
    size = 0
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8
               }
    for item in pi_func:
        if n <= item:
            size = pi_func[item]
            break
    array = [_ for _ in range(size)]
    array[1] = 0
    i = 2
    p = 2
    cnt = 1
    while cnt <= n:
        if array[i] != 0:
            p = array[i]
            cnt += 1
            j = i * 2
            while j < size:
                array[j] = 0
                j += i
        i += 1
    return p

# timeit:
# 0.038070099999999996 = 100
# 0.3536904 = 200
# 0.38599239999999996 = 400
# 0.445534 = 800
# cProfile
#  1    0.000    0.000    0.000    0.000 task_2.py:10(sieve) = 100
#  1    0.003    0.003    0.003    0.003 task_2.py:10(sieve) = 200
#  1    0.003    0.003    0.004    0.004 task_2.py:10(sieve) = 400
#  1    0.004    0.004    0.005    0.005 task_2.py:10(sieve) = 800

# без использования «Решета Эратосфена»


def prime(n):
    cnt = 1
    p = 2
    while cnt < n:
        p += 1
        for i in range(2, p):
            if p % i == 0:
                break
        else:
            cnt += 1
    return p

# timeit:
# 0.21924049999999998 = 100
# 1.0396311999999999 = 200
# 4.8981745000000005 = 400
# 21.809254900000003 = 800
# cProfile
#  1    0.002    0.002    0.002    0.002 task_2.py:51(prime) = 100
#  1    0.011    0.011    0.011    0.011 task_2.py:51(prime) = 200
#  1    0.047    0.047    0.047    0.047 task_2.py:51(prime) = 400
#  1    0.215    0.215    0.215    0.215 task_2.py:51(prime) = 800


s = """
def sieve(n):
    size = 0
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8
               }
    for item in pi_func:
        if n <= item:
            size = pi_func[item]
            break
    array = [_ for _ in range(size)]
    array[1] = 0
    i = 2
    p = 2
    cnt = 1
    while cnt <= n:
        if array[i] != 0:
            p = array[i]
            cnt += 1
            j = i * 2
            while j < size:
                array[j] = 0
                j += i
        i += 1
    return p
sieve(800)
"""
print(timeit.timeit(s, number=100))
cProfile.run('sieve(800)')

# print(sieve(5))
# print(prime(5))
