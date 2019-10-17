# Задание - 3:
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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
array[max_pos], array[min_pos] = array[min_pos], array[max_pos]
print(f"Result array: {array}")
