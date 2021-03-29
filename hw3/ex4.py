def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    result = 1
    while y < 0:
        result *= x
        y += 1
    return 1 / result


print(my_func(2.5, -5))
print(my_func_2(2.5, -5))

