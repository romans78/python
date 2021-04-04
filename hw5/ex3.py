with open("salaries.txt", encoding="utf-8") as salaries:
    salary_by_employee = {line[0]: float(line[1]) for line in map(lambda l: l.split(), salaries.readlines())}

print("Сотрудники получающие менее 20000:",
      *[fn for fn in salary_by_employee.keys() if salary_by_employee.get(fn) < 20000], sep="\n")

print(f"Средний доход сотрудников составляет {sum(salary_by_employee.values()) / len(salary_by_employee):.2f}")
