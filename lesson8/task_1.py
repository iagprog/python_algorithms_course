# Задание - 1.
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def subs_num(s):
    res = [hashlib.sha1(s[i:j].encode("UTF-8")).hexdigest()
           for i in range(len(s) + 1)
           for j in range(i, len(s) + 1)
           if s[i:j] != '' and len(s[i:j]) != len(s)]
    return len(set(res))


s = input("Введите строку: ")
print(f"Количество подстрок: {subs_num(s)}")


