# Задача-2.
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


# возьмем 10 случайных вещественных чисел на промежутке [0;50)
array = [round(random.random()*50, 2) for _ in range(10)]


def merge_sort(a):
    size = len(a)
    if size < 2:
        return a
    m = size // 2
    left_part = merge_sort(a[:m])
    right_part = merge_sort(a[m:])
    return merge(left_part, right_part)


def merge(left_part, right_part):
    res = []
    while left_part and right_part:        # пока есть элементы в списках
        if left_part[0] <= right_part[0]:  # попарно сравниваем
            res.append(left_part[0])
            left_part = left_part[1:]      # удаляем из списка
        else:
            res.append(right_part[0])
            right_part = right_part[1:]
    if left_part:                    # если что-то осталось в одном из списков - добавляем в конец
        res += left_part
    else:
        res += right_part
    return res


print(f"Исходный массив: \n{array}")
print(f"Результат сортировки: \n{merge_sort(array)}")
