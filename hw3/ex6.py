def int_func(string):
    return string.capitalize()


string = input("Введите строку из слов, разделённых пробелом: ")

print(" ".join(map(int_func, string.split())))
