n_elements = int(input("Введите число элементов в списке: "))
lst = []
while n_elements > 0:
    lst.append(input("Добавьте элемент в список: "))
    n_elements -= 1

print("Текущий список элементов:", lst)
for i in range(1, len(lst) - 1, 2):
    temp = lst[i]
    lst[i] = lst[i - 1]
    lst[i - 1] = temp

print("Cписок элементов после обена значений:", lst)
