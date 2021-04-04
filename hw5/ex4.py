en_ru_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("en_numbers.txt") as en_numbers:
    with open("ru_numbers.txt", "w", encoding="utf-8") as ru_numbers:
        for line in en_numbers.readlines():
            split_line = line.split("-")
            ru_numbers.write(en_ru_dict.get(split_line[0]) + "-" + split_line[1])
