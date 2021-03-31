from sys import argv


def calculate_salary(hours, hour_rate, bonus):
    return hours * hour_rate + bonus


hours, hour_rate, bonus = tuple(map(float, argv[1:]))
print(f"Заработная плата составляет {calculate_salary(hours, hour_rate, bonus):.2f}")
