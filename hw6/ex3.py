class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position)
        self._income.update({"wage": wage, "bonus": bonus})

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


pos1 = Position("Дмитрий", "Степанов", "бухгалтер", 30000, 20000)
pos2 = Position("Алла", "Букова", "главный бухгалтер", 70000, 50000)
pos3 = Position("Андрей", "Петров", "финансовый директор", 200000, 250000)

positions = [pos1, pos2, pos3]

for pos in positions:
    print(f"Общий доход сотрудника по имени {pos.get_full_name()} составляет {pos.get_total_income()} рублей")
