with open("file.txt", "w", encoding="utf-8") as out_file:
    str = input("Введите строку: ")
    while str != "":
        out_file.write(str + "\n")
        str = input("Введите строку: ")


print("\nСодержимое файла:")
with open("file.txt", encoding="utf-8") as in_file:
    print(*in_file.readlines(), sep='')
