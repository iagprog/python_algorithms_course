# Задача-2: Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input("Введите натуральное число: "))
even = 0
odd = 0
if a == 0:
    even = 1
else:
    while a != 0:
        c = a % 10 % 2
        if c == 0:
            even += 1
        else:
            odd += 1
        a = a // 10
print(f"Количество четных цифр натурального числа: {even}")
print(f"Количество нечетных цифр натурального числа: {odd}")
