# Задача-3: По введенным пользователем координатам двух точек
# вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

print("Задача-3.")
print("Введите координаты двух точек.")
x1 = float(input("Введите координату x первой точки: "))
y1 = float(input("Введите координату y первой точки: "))
x2 = float(input("Введите координату x второй точки: "))
y2 = float(input("Введите координату y второй точки: "))
if x1 != x2:
    k = round((y1 - y2) / (x1 - x2), 2)
    b = round((y1 - k * x1), 2)
    print(f"Уравнение имеет вид: y = {k}x + {b}")
else:
    print(f"Уравнение имеет вид: x = {x1}")
