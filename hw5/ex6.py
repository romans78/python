with open("classes.txt", encoding="utf-8") as classes:
    lines = classes.readlines()

subject_dict = {}
for line in lines:
    subject = line.split(":")[0]
    line = line.replace(":", " ").replace("(", " ").replace(")", " ").replace("-", " ")
    subject_dict.update({subject: sum(map(lambda s: int(s) if str.isnumeric(s) else 0, line.split()))})

print(subject_dict)
