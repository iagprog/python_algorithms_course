# Задание - 7:
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min1 = array[0]
min2 = array[1]
pos = 0
for i in range(2, SIZE):
    if array[i] < min1:
        if min1 < min2:
            min2 = min1
        min1 = array[i]
    elif array[i] < min2:
        min2 = array[i]
print(f"Array: {array}")
print(f"First min = {min1}, second min = {min2}.")
