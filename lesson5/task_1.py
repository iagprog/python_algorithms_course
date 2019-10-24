# Задача -1.
# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.


firms = {}  # в словарь будем записывать имена организаций и прибыль за год
profit = [0, 0, 0, 0]  # профит по кварталам
all_profit = 0
num = int(input("Введите количество предприятий: "))
for i in range(num):
    name = input(f"Введите имя {i + 1} предприятия: ")
    for j in range(4):
        profit[j] = float(input(f"Введите прибыль за {j + 1} квартал: "))
    year_profit = sum(profit)
    firms[name] = year_profit
    all_profit += year_profit
average = all_profit / num
print(f"Средняя прибыль за год для всех предприятий: {round(average, 2)}")
print("Наименования предприятий, чья прибыль выше среднего: ")
for key in firms:
    if firms[key] > average:
        print(key)
print("Наименования предприятий, чья прибыль ниже среднего: ")
for key in firms:
    if firms[key] < average:
        print(key)
