class OfficeEquipmentWarehouse:
    pass


class OfficeEquipment:
    def __init__(self, id, name, weight, size, color):
        self.id = id
        self.name = name
        self.weight = weight
        self.size = size
        self.color = color

    def __str__(self):
        return self.name + " id = " + str(self.id)


class Printer(OfficeEquipment):
    def __init__(self, id, weight, size, color, paper_sizes, resolution, paper_per_minute, type, paper_capacity):
        super().__init__(id, "printer", weight, size, color)
        self.paper_sizes = paper_sizes
        self.resolution = resolution
        self.paper_per_minute = paper_per_minute
        self.type = type
        self.paper_capacity = paper_capacity


class Scanner(OfficeEquipment):
    def __init__(self, id, weight, size, color, resolution, color_depth, paper_capacity):
        super().__init__(id, "scanner", weight, size, color)
        self.resolution = resolution
        self.color_depth = color_depth
        self.paper_capacity = paper_capacity


class Fax(OfficeEquipment):
    def __init__(self, id, weight, size, color, paper_capacity, memory_size):
        super().__init__(id, "fax", weight, size, color)
        self.paper_capacity = paper_capacity
        self.memory_size = memory_size
