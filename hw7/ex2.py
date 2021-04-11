from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def material_consumption(self):
        pass

    @abstractmethod
    def type(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 38:
            self.__size = 38
        elif size > 62:
            self.__size = 62
        else:
            self.__size = size

    @property
    def type(self):
        return "пальто"

    def material_consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            self.__height = 100
        elif height > 300:
            self.__height = 300
        else:
            self.__height = height

    @property
    def type(self):
        return "костюм"

    def material_consumption(self):
        return self.height * 2 + 0.3


coat = Coat(42)
costume = Costume(178)

coat2 = Coat(70)
costume2 = Costume(10)

clothes = [coat, costume, coat2, costume2]

for clt in clothes:
    print(
        f"Расход материала на {clt.type} для {f'роста {clt.height}' if clt.type == 'костюм' else f'размера {clt.size}'}"
        f" равен {clt.material_consumption()}")
