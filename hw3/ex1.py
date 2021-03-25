def division(x, y):
    if y == 0.0:
        return "Ошибка, деление на ноль"
    return x / y


x = float(input("Введите первое число (делимое): "))
y = float(input("Введите второе число (делитель): "))

print("Результат деления:", division(x, y))
