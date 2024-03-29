# Задача-1: Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

sign = '1'
while sign != '0':
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    sign = input("Введите знак операции ('0' - завершить программу, '+', '-', '*', '/'): ")
    if sign == '+':
        n = a + b
        print(f"Результат операции: {n}")
    elif sign == '-':
        n = a - b
        print(f"Результат операции: {n}")
    elif sign == '*':
        n = round(a * b, 2)
        print(f"Результат операции: {n}")
    elif sign == '/':
        if b != 0:
            n = round(a / b, 2)
            print(f"Результат операции: {n}")
        else:
            print("Оишбка! Деление на 0 невозможно.")
    elif sign != '0':
        print("Ошибка! Введите верный знак операции.")
