class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.img * other.img,
                             self.real * other.img + self.img * other.real)

    def __str__(self):
        return str(self.real) + (" + " if self.img >= 0 else " - ") + str(abs(self.img)) + "i"


c1 = ComplexNumber(3, -4)
c2 = ComplexNumber(1, 1)
c3 = ComplexNumber(0, 4)
c4 = ComplexNumber(5, 0)

print(c1, c2, c3, c4, sep="\n")
print(c1 + c3)
print(c4 * c2)
print(ComplexNumber(-2, 0) * c2 + c3)
