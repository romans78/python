class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_image = ""
        max_len = max(list(map(lambda x: max(list(map(lambda y: len(str(y)), x))), self.matrix)))
        for row in self.matrix:
            for cell in row:
                matrix_image += f"{cell:<{max_len}} "
            matrix_image += "\n"
        return matrix_image

    def __add__(self, other):
        matrix_sum = list(map(lambda pair: [sum(p) for p in zip(pair[0], pair[1])], zip(self.matrix, other.matrix)))
        return Matrix(matrix_sum)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1023, 11, 12]])

m2 = Matrix([[10, 2, 3], [7, 6, 5], [7, 0, 9], [23, 101, 2]])

print(m1 + m2)
print()
print(m2 + m1)
