n_month = 0
while not (1 <= n_month <= 12):
    n_month = int(input("Введите номер месяца (от 1 до 12): "))

# Начинаем год с марта с индексом 0
n_month = ((n_month - 1) + 10) % 12

season_list = ["весна", "лето", "осень", "зима"]
season_dict = dict(enumerate(season_list))

print("Время года согласно списку:", season_list[n_month // 3])
print("Время года согласно словарю:", season_dict.get(n_month // 3))
