# Задание - 4:
# Определить, какое число в массиве встречается чаще всего.

import random


SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
num = array[0]
max_count = 0
for i, item in enumerate(array):
    count = 0
    for j in range(i + 1, SIZE):
        if array[j] == item:
            count += 1
    if count > max_count:
        num = item
        max_count = count
print(f"Array: {array}")
if max_count:
    print(f"Result number: {num}")
else:
    print("All numbers have the same frequency.")
