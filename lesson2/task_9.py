# Задача-9: Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

max_num = 0
max_digits = 0
n = int(input("Введите количество натуральных чисел: "))
for i in range(n):
    a = int(input(f"Введите {i+1} число: "))
    tmp_num = a
    tmp_digits = 0
    while tmp_num % 10:
        tmp_digits += tmp_num % 10
        tmp_num //= 10
    if tmp_digits > max_digits:
        max_digits = tmp_digits
        max_num = a
print(f"Наибольшее число по сумме цифр: {max_num}, сумма цифр этого числа: {max_digits}.")
