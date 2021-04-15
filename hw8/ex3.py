class NotNumberException(Exception):
    def __init__(self, txt):
        self.txt = f"{txt} не является числом"

    def __str__(self):
        return self.txt


elements = []
while True:
    try:
        el = input("Введите элемент списка: ")
        if el == 'stop':
            break
        if not el.isnumeric():
            raise NotNumberException(el)
    except NotNumberException as nne:
        print(nne)
    else:
        elements.append(int(el))


print(elements)
