numbers = "1 76 32 43.5 456 32 44 -17.5 -0.7 1.234"
with open("numbers.txt", "w") as nums:
    nums.write(numbers)

with open("numbers.txt") as nums:
    print(f"Сумма чисел в файле равна {sum(map(float, nums.readline().split()))}")
