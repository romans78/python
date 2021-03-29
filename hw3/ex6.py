def int_func(string):
    return chr(ord(string[0]) - 32) + string[1:]


string = input("Введите строку из слов, разделённых пробелом: ")

print(" ".join(map(int_func, string.split())))