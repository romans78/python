class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        super().__init__("ручка")

    def draw(self):
        print("Рисунок ручкой")


class Pencil(Stationery):
    def __init__(self):
        super().__init__("карандаш")

    def draw(self):
        print("Рисунок карандашом")


class Handle(Stationery):
    def __init__(self):
        super().__init__("маркер")

    def draw(self):
        print("Рисунок маркером")


stationery = Stationery("канцелярская принадлежность")
pen = Pen()
pencil = Pencil()
handle = Handle()

stationeries = [stationery, pen, pencil, handle]

for stat in stationeries:
    print(f"{stat.title.capitalize()}")
    stat.draw()
