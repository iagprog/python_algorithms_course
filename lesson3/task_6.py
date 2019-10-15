# Задание - 6:
# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_num = array[0]
max_num = array[0]
min_pos = 0
max_pos = 0
for i, item in enumerate(array):
    if item < min_num:
        min_num = item
        min_pos = i
    if item > max_num:
        max_num = item
        max_pos = i
print(f"Array: {array}")
print(f"max_num = {max_num}, pos = {max_pos}")  # оставил для проверки результата
print(f"min_num =  {min_num}, pos = {min_pos}")
if max_pos < min_pos:
    max_pos, min_pos = min_pos, max_pos
res = 0
for i in range(min_pos + 1, max_pos):
    res += array[i]
print(f"Result sum between {array[min_pos]} and {array[max_pos]}: {res}")
