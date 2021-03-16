# 1.
a = 10
b = "string"
c = 0.5
d = [2, "a", 3.5]

print("a =", a, " b =", b, " c =", c, " d =", d)

month_map = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
             9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}

year_of_birth = int(input("Введите год рождения: "))
month_of_birth = int(input("Введите номер месяца рождения: "))
day_of_birth = int(input("Введите номер дня рождения: "))

first_name = input("Введите Ваше имя: ")
last_name = input("Введите Вашу фамилию: ")

print(f"Здравствуйте, {first_name} {last_name}!")
print(f"Ваш год рождения: {year_of_birth}")
print(f"Ваш месяц рождения: {month_map[month_of_birth]}")
print(f"Ваш день рождения: {day_of_birth}")

# 2.
minus = ""
seconds = int(input("Введите время в секундах: "))
if seconds < 0:
    seconds = -seconds
    minus = "-"
print(f"Вы ввели {minus}{seconds // 3600:0>2}:{(seconds % 3600) // 60:0>2}:{(seconds % 3600) % 60:0>2}")

#3.
number = int(input("Введите число: "))
print(f"Получилось: {number + int(str(number) * 2) + int(str(number) * 3)}")



#4.
number = int(input("Введите целое положительное число: "))

max_digit = 0

while number > 0:
    if (number % 10) > max_digit:
        max_digit = number % 10
    if max_digit == 9:
        break
    number //= 10

print("Самая большая цифра в числе - ", max_digit)


# 5.
revenue = int(input("Введите размер выручки фирмы: "))
expenses = int(input("Введите размер издержек фирмы: "))

profit = revenue - expenses

if profit > 0:
    print("Фирма получила прибыль")
    print(f"Рентабельность фирмы составила {profit / expenses:.2f}")
    n_workers = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника составила {profit / n_workers:.2f}")

elif profit < 0:
    print("Фирма осталась в убытке")
else:
    print("Выручка фирмы равна её издержкам")

# 6.
from math import log, ceil

a = float(input("Введите результат в километрах в первый день: "))
b = float(input("Введите необходимое количество километров: "))

n_day = 1
if a < b:
    n_day += ceil(log(b/a, 1.1))
print("Номер дня:", n_day)