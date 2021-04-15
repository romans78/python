class OfficeEquipmentWarehouse:
    def __init__(self):
        self.__storage = dict()
        self.__depts = dict()

    def get_office_equipment(self, office_eq_type, n_units):
        if self.__storage.get((office_eq_type.name, office_eq_type.id)) == None:
            self.__storage.update({(office_eq_type.name, office_eq_type.id): n_units})
        else:
            self.__storage.update(
                {(office_eq_type.name, office_eq_type.id): self.__storage.get(
                    (office_eq_type.name, office_eq_type.id)) + n_units})

    def send_office_equipment_to_dept(self, office_eq_type, n_units, dept):
        self.get_office_equipment(office_eq_type, -n_units)
        if self.__depts.get(dept) == None:
            self.__depts.update({dept: {(office_eq_type.name, office_eq_type.id): n_units}})
        else:
            if self.__depts.get(dept).get((office_eq_type.name, office_eq_type.id)) == None:
                self.__depts.get(dept).update({(office_eq_type.name, office_eq_type.id): n_units})
            else:
                self.__depts.get(dept).update(
                    {(office_eq_type.name, office_eq_type.id):
                         self.__depts.get(dept).get((office_eq_type.name,
                                                     office_eq_type.id)) + n_units})

    def __str__(self):
        return "Текущее состояние склада\n" + str(self.__storage) + "\n\nПолучено отделами компании\n" + str(
            self.__depts)


class OfficeEquipment:
    def __init__(self, id, name, weight, size, color):
        self.id = id
        self.name = name
        self.weight = weight
        self.size = size
        self.color = color

    def __str__(self):
        return self.name + " id = " + str(self.id)

    def validate(self):
        if not isinstance(self.id, int):
            print("переменная id должна быть числом")
        if not isinstance(self.weight, int):
            print("переменная weight должна быть числом")
        if not isinstance(self.size, int):
            print("переменная size должна быть числом")
        if not isinstance(self.name, str):
            print("переменная name должна быть строковой")
        if not isinstance(self.color, str):
            print("переменная color должна быть строковой")


class Printer(OfficeEquipment):
    def __init__(self, id, weight, size, color, paper_sizes, resolution, paper_per_minute, type, paper_capacity):
        super().__init__(id, "printer", weight, size, color)
        self.paper_sizes = paper_sizes
        self.resolution = resolution
        self.paper_per_minute = paper_per_minute
        self.type = type
        self.paper_capacity = paper_capacity
        self.validate()

    def validate(self):
        super().validate()
        if not isinstance(self.paper_sizes, tuple):
            print("переменная paper_sizes должна быть списком")
        if not isinstance(self.resolution, int):
            print("переменная resolution должна быть числом")
        if not isinstance(self.paper_per_minute, int):
            print("переменная paper_per_minute должна быть числом")
        if not isinstance(self.type, str):
            print("переменная type должна быть строковой")
        if not isinstance(self.paper_capacity, int):
            print("переменная paper_capacity должна быть v")


class Scanner(OfficeEquipment):
    def __init__(self, id, weight, size, color, resolution, color_depth, paper_capacity):
        super().__init__(id, "scanner", weight, size, color)
        self.resolution = resolution
        self.color_depth = color_depth
        self.paper_capacity = paper_capacity
        self.validate()

    def validate(self):
        super().validate()
        if not isinstance(self.resolution, int):
            print("переменная resolution должна быть числом")
        if not isinstance(self.color_depth, int):
            print("переменная color_depth должна быть числом")
        if not isinstance(self.paper_capacity, int):
            print("переменная paper_capacity должна быть числом")


class Fax(OfficeEquipment):
    def __init__(self, id, weight, size, color, paper_capacity, memory_size):
        super().__init__(id, "fax", weight, size, color)
        self.paper_capacity = paper_capacity
        self.memory_size = memory_size
        self.validate()

    def validate(self):
        super().validate()
        if not isinstance(self.paper_capacity, int):
            print("переменная paper_capacity должна быть числом")
        if not isinstance(self.memory_size, int):
            print("переменная memory_size должна быть числом")


pr1 = Printer(1, 5, 10, "white", ("A4", "A3"), 150, 10, "laser", 1000)
pr2 = Printer(2, 3, 10, "red", ("A4",), 150, 5, "laser", 500)
sc1 = Scanner(3, 5, 7, "white", 140, 50, 50)
sc2 = Scanner(4, 10, 12, "gray", 180, 100, 100)
fax1 = Fax(5, 2, 3, "black", 100, 15)

warehouse = OfficeEquipmentWarehouse()
warehouse.get_office_equipment(pr1, 10)
warehouse.get_office_equipment(pr2, 50)
warehouse.get_office_equipment(sc1, 30)
warehouse.get_office_equipment(sc2, 40)
warehouse.get_office_equipment(fax1, 20)
warehouse.get_office_equipment(pr1, 10)

print(warehouse)

warehouse.send_office_equipment_to_dept(pr1, 5, "finance")
warehouse.send_office_equipment_to_dept(pr2, 5, "finance")
warehouse.send_office_equipment_to_dept(pr1, 3, "finance")
warehouse.send_office_equipment_to_dept(sc2, 7, "material management")
warehouse.send_office_equipment_to_dept(sc1, 5, "CEO office")
warehouse.send_office_equipment_to_dept(fax1, 5, "material management")
warehouse.send_office_equipment_to_dept(pr2, 5, "finance")

print(warehouse)

Printer(1, 5, "10", 5, "A4", 150, 10, ("laser",), "1000")
Fax(5, 2, 3, 7, "100", "15")
Scanner(3, 5, 7, 10, 140, "50", 50)
