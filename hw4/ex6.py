from itertools import count, cycle

# a итератор, генерирующий целые числа, начиная с указанного
n = 5

for i in count(n):
    if i > 10:
        break
    print(i)

print()

# б итератор, повторяющий элементы некоторого списка, определенного заранее

lst = ["a", 1, [4, 5], "text", {1: "a", 2: "b"}]
counter = 0
j = 0
for i in cycle(lst):
    j += 1
    print(i, end=" ")
    if j == len(lst):
        counter += 1
        print()
        j = 0
    if counter >= 3:
        break
