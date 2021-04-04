with open("file.txt", encoding="utf-8") as in_file:
    lines = in_file.readlines()
    n_lines = len(lines)
    n_words_in_lines = map(lambda l: len(l.split()), lines)
    print(f"Файл содержит {n_lines} строк")
    print("Количество слов в каждой строке:")
    print(*list(map(lambda l: "строка " + str(l[0]) + ": " + str(l[1]), enumerate(n_words_in_lines, start=1))),
          sep="\n")
