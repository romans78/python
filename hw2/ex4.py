str = input("Введите строку: ")

for n, s in enumerate(str.split()):
    print(n, ":", s[:10])
