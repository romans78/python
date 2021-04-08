class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_asphalt_mass(self, asphalt_density_per_cm, thickness_cm):
        mass = self.__length * self.__width * asphalt_density_per_cm * thickness_cm / 1000
        print(f"Масса асфальта равна {mass} тонн")


road = Road(5000, 20)
road.calculate_asphalt_mass(25, 5)
