# Задание - 9:
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random


SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
print(*matrix, sep='\n')
max_el = 0
for i in range(SIZE):
    min_el = matrix[0][i]
    for j in range(SIZE):
        if matrix[j][i] < min_el:
            min_el = matrix[j][i]
    if max_el == 0:
        max_el = min_el
    elif min_el > max_el:
        max_el = min_el
print(f"Max element among the min elements of the matrix columns: {max_el}")
