class ZeroDivisionException(Exception):
    def __init__(self):
        self.txt = "Ошибка. Деление на ноль"

    def __str__(self):
        return self.txt


try:
    in_data = input("Введите два числа (через пробел): ")
    a, b = map(int, in_data.split())
    if b == 0:
        raise ZeroDivisionException()
except ZeroDivisionException as zde:
    print(zde)
else:
    print(f"Результат деления первого числа на второе равен {a / b}")
