# Задание - 5:
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random


SIZE = 10
MIN_ITEM = -50
MAX_ITEM = 50
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_negative = 0
pos = 0
for i, item in enumerate(array):
    if item < 0:
        if max_negative == 0:
            max_negative = item
        else:
            if item > max_negative:
                max_negative = item
                pos = i
print(f"Array: {array}")
if max_negative:
    print(f"Max negative number = {max_negative}, position = {pos}.")
else:
    print(f"There is no negative numbers.")
