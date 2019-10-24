# Задача -2.
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque  # используется при смещении разрядов и добавлении в список слева


def hex_to_num(num):  # функция конвертирует буквы из словаря в соотв. числа
    for i, item in enumerate(num):
        if item in letter_value:
            num[i] = letter_value[item]
    return num


def num_to_hex(num):  # функция конвертирует числа > 9 в  соотв. буквы из словаря
    for i, item in enumerate(num):
        for key in letter_value:
            if letter_value[key] == item:
                num[i] = key
    return num


def addition(a, b):          # функция сложения
    a = hex_to_num(a)
    b = hex_to_num(b)
    a = list(map(int, a))   # все числовые символы в цифры
    b = list(map(int, b))
    if len(b) > len(a):     # прибавляем к более длинному числу
        a, b = b, a
    a.reverse()             # разворачиваем для сложения в столбик
    b.reverse()
    for i in range(len(b)):
        n = a[i] + b[i]
        a[i] = n % 16
        if n >= 16:
            if i + 1 == len(a):  # нужно добавить ведущий разряд
                a.append(1)      # число развернутое, так что добавляем в конец
            else:
                a[i + 1] += 1
    a.reverse()
    a = num_to_hex(a)
    return a


def multiplication(a, b):   # функция умножения
    res = [0]
    a = hex_to_num(a)
    b = hex_to_num(b)
    a = list(map(int, a))  # все числовые символы в цифры
    b = list(map(int, b))
    if len(a) < len(b):
        a, b = b, a
    a.reverse()
    b.reverse()
    print(a, b)
    for i, b1 in enumerate(b):
        d = 0
        new = deque()
        for a1 in a:
            n = a1 * b1 + d         # умножаем и добавляем перенос из прошлого разряда
            d = n // 16             # что переносим в следующий разряд
            f = n % 16
            new.extendleft([f])     # записываем в разряд
        if d:                       # если остался перенос с другого разряда
            new.extendleft([d])

        if i > 0:                   # проверяем есть ли следующий результат умножения
            new += [0] * i          # добавляем 0 для сноса следующего суммируемого числа влево
        else:                       # иначе первое слагаемое
            res = list(new)
            continue
        res = addition(list(new)[:], res)  # суммируем результаты умножения
    return res


a = list(input("Введите первое шестнадцатеричное число: "))
b = list(input("Введите второе шестнадцатеричное число: "))
letter_value = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
print(f"Результат сложения:  {addition(a[:], b[:])}")
print(f"Результат умножения: {(multiplication(a[:], b[:]))}")
