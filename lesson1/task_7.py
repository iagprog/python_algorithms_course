# Задача-7: По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

print("Задача-7.")
print("Введите длины трех отрезков.")
a = float(input("Введите длину первого отрезка: "))
b = float(input("Введите длину второго отрезка: "))
c = float(input("Введите длину третьего отрезка: "))
if (a + b) > c and (a + c) > b and (b + c) > a:
    if a == b and b == c:
        print("Треугольник равносторонний.")
    elif a == b or a == c or b == c:
        print("Треугольник равнобедренный.")
    else:
        print("Треугольник разносторонний.")
else:
    print("Треугольник не существует.")
