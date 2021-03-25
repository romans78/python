total = 0
flag = True


def calculate_total(string, end_symbol='!'):
    string = string.strip()
    if end_symbol in string:
        global flag
        flag = False
        if string[0] == end_symbol:
            return
        string = string.split(end_symbol)[0]
    numbers = string.split()
    numbers = list(map(float, numbers))
    global total
    total += sum(numbers)
    return total


while flag:
    result = calculate_total(input("Введите строку чисел, разделённых пробелом (! - для выхода): "))
    if result is not None:
        print(f"Общая сумма: {result}")
