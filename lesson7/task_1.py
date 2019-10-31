# Задача-1.
# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random


array = [round(random.randint(-100, 99)) for _ in range(10)]
random.shuffle(array)

# проходы во внутреннем цикле можно уменьшить, отнимая j "пузырьков",
# т.к. j "пузырьков" в конце массива уже отсортированы


def bubble_sort(a):
    size = len(a)
    for j in range(1, size):
        for i in range(size-j):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


print(f"Исходный массив: \n{array}")
print(f"Результат сортировки: \n{bubble_sort(array)}")
