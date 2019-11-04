# Задача - 1:
# Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Для анализа выбрана задача 9 из урока 2:
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# # Вывести на экран это число и сумму его цифр.
# разрядность ОС 64-bit, интерпретатор python 3.7 64-bit

# для определения памяти переменных используется locals(), которая возвращает словарь локальных переменных
# дальше берутся значения по ключам и отправляются на иссоедование рекурсивной функции show_size().
# каждый алгоритм представлен в виде функции (test1(), test2(), test3())
# также можно было получить список параметров с помошью dir():
"""
d = dir()
for i in d:
    if ('__' not in i) and ('sys' not in i) and ('show_size' not in i):
        show_size(eval(i))
"""

import sys
from collections import namedtuple
from collections import defaultdict


# тестовый ввод для test1(), test2(), test3():
# Введите количество натуральных чисел: 2
# Введите 1 число: 33
# Введите 2 число: 44


def test1():
    max_num = 0
    max_digits = 0
    n = int(input("Введите количество натуральных чисел: "))
    for i in range(n):
        a = int(input(f"Введите {i + 1} число: "))
        tmp_num = a
        tmp_digits = 0
        while tmp_num % 10:
            tmp_digits += tmp_num % 10
            tmp_num //= 10
        if tmp_digits > max_digits:
            max_digits = tmp_digits
            max_num = a
    print(f"Наибольшее число по сумме цифр: {max_num}, сумма цифр этого числа: {max_digits}.")
    print("test1:")                 # анализируем алгоритм
    res = 0
    for obj in locals().values():
        res += show_size(obj)
    print(f"Total size = {res}")

# test1:
# type=<class 'int'>, size=28, obj=44
# type=<class 'int'>, size=28, obj=8
# type=<class 'int'>, size=28, obj=2
# type=<class 'int'>, size=28, obj=1
# type=<class 'int'>, size=28, obj=44
# type=<class 'int'>, size=24, obj=0
# type=<class 'int'>, size=28, obj=8
# type=<class 'int'>, size=24, obj=0
# Total size = 216


def test2():
    n = int(input("Введите количество натуральных чисел: "))
    all_nums = []
    max_num = 0
    max_digits = 0
    N = namedtuple('N', 'num, sum_res')
    for i in range(n):
        n = input(f"Введите {i+1} число: ")
        all_nums.append(N(int(n), sum(map(int, list(n)))))
    for one_num in all_nums:
        if one_num.sum_res > max_num:
            max_num = one_num.num
            max_digits = one_num.sum_res
    print(f"Наибольшее число по сумме цифр: {max_num}, сумма цифр этого числа: {max_digits}.")
    print("test2:")
    res = 0                         # анализируем алгоритм
    for obj in locals().values():
        res += show_size(obj)
    print(f"Total size = {res}")

# test2:
# type=<class 'str'>, size=51, obj=44
# type=<class 'list'>, size=96, obj=[N(num=33, sum_res=6), N(num=44, sum_res=8)]
# type=<class '__main__.N'>, size=64, obj=N(num=33, sum_res=6)
# type=<class 'int'>, size=28, obj=33
# type=<class 'int'>, size=28, obj=6
# type=<class '__main__.N'>, size=64, obj=N(num=44, sum_res=8)
# type=<class 'int'>, size=28, obj=44
# type=<class 'int'>, size=28, obj=8
# type=<class 'int'>, size=28, obj=33
# type=<class 'int'>, size=28, obj=6
# type=<class 'type'>, size=888, obj=<class '__main__.N'>
# type=<class 'int'>, size=28, obj=1
# type=<class '__main__.N'>, size=64, obj=N(num=44, sum_res=8)
# type=<class 'int'>, size=28, obj=44
# type=<class 'int'>, size=28, obj=8
# type=<class 'int'>, size=24, obj=0
# Total size = 1207


# вариант 3: с использованием коллекции defaultdict

def test3():
    max_num = 0
    max_digits = 0
    all_nums = defaultdict(list)
    n = int(input("Введите количество натуральных чисел: "))
    for i in range(n):
        n = input(f"Введите {i + 1} число: ")
        all_nums[int(n)].append(sum(map(int, list(n))))
    for one_num in all_nums:
        if all_nums[one_num][0] > max_num:
            max_num = all_nums[one_num][0]
            max_digits = all_nums[one_num][0]
    print(f"Наибольшее число по сумме цифр: {max_num}, сумма цифр этого числа: {max_digits}.")

    print("test3:")                 # анализируем алгоритм
    res = 0
    for obj in locals().values():
        res += show_size(obj)
    print(f"Total size = {res}")

# test3:
# type=<class 'int'>, size=28, obj=8
# type=<class 'int'>, size=28, obj=8
# type=<class 'collections.defaultdict'>, size=248, obj=defaultdict(<class 'list'>, {33: [6], 44: [8]})
# type=<class 'int'>, size=28, obj=33
# type=<class 'list'>, size=96, obj=[6]
# type=<class 'int'>, size=28, obj=6
# type=<class 'int'>, size=28, obj=44
# type=<class 'list'>, size=96, obj=[8]
# type=<class 'int'>, size=28, obj=8
# type=<class 'str'>, size=51, obj=44
# type=<class 'int'>, size=28, obj=1
# type=<class 'int'>, size=28, obj=44
# type=<class 'int'>, size=24, obj=0
# Total size = 435

# функция рекурсивно возвращает размеры переменных


def show_size(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):  # тест на словарь
            for key, value in x.items():
                show_size(key)
                show_size(value)
        elif not (isinstance(x, str) or isinstance(x, type)):
            for item in x:
                show_size(item)
    return sys.getsizeof(x)


test1()
test2()
test3()

# Вывод: алгоритмы 2 и 3 с использованием коллекций занимают много места в памяти,
# т.к. резервируют дополнительное место под переменные + для вычислений использованы списки,
# которые также занимают дополнительное место.
# В программе с использованием остатка от деления всего лишь несколько целочисленных переменных для
# вычисления и промежуточных результатов, поэтому памяти расходуется в разы меньше.
