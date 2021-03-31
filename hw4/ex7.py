def fact(n):
    counter = 1
    result = 1
    while counter <= n:
        yield result
        counter += 1
        result *= counter


for i in fact(10):
    print(i)

