# Задание - 8:
# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

SIZE = 5
matrix = []
print("Fill in the matrix.")
print("Enter 3 digits separated by a space in each of 5 lines.")
for i in range(SIZE):
    a = list(map(float, input(f"{i} row: ").split()))
    sum_el = 0
    for el in a:
        sum_el += el
    a.append(sum_el)
    matrix.append(a)
print("Result matrix (5*4): ")
print(*matrix, sep='\n')
