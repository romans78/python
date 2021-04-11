class Cell:
    def __init__(self, n_cells):
        if n_cells < 0:
            n_cells = 0
        self.n_cells = n_cells

    def __add__(self, other):
        return Cell(self.n_cells + other.n_cells)

    def __sub__(self, other):
        if other.n_cells > self.n_cells:
            print("Количество ячеек не может быть отрицательным")
            return None
        return Cell(self.n_cells - other.n_cells)

    def __mul__(self, other):
        return Cell(self.n_cells * other.n_cells)

    def __truediv__(self, other):
        #С учётом того факта, что round в питоне не является классическим округлением
        #Округление в критических ситуациях происходит к ближайшему чётному числу
        #Например, round(4.5) = 4, а не 5 как можно было бы ожидать, но round(5.5) = 6, как ожидалось
        return Cell(round(self.n_cells / other.n_cells))


    def make_order(cell, n_cells_in_row):
        result = ""
        n_cells = cell.n_cells
        while True:
            if n_cells_in_row < n_cells:
                result += '*' * n_cells_in_row + '\n'
                n_cells -= n_cells_in_row
            else:
                result += '*' * n_cells
                return result


c1 = Cell(20)
c2 = Cell(37)

print(Cell.make_order(c1, 5))
print()
print(Cell.make_order(c2, 7))
print()
print(Cell.make_order(c1 + c2, 6))
print()
print(Cell.make_order(c2 - c1, 3))
print()
print(Cell.make_order(c1 * c2, 100))
print()
print(Cell.make_order(c2 / c1, 4))
print()
c3 = c1 - c2
print(c3)


