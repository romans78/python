lst = [125, 62, 33, 33, 7, 7, 7, 5]
print("Текущий рейтинг:", lst)

new_element = int(input("Введите новый элемент рейтинга: "))

lst.append(new_element)
lst.sort(reverse=True)

print("Новый рейтинг:", lst)
