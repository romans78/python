class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("машина поехала")

    def stop(self):
        print("машина остановилась")

    def turn(self, direction):
        print(f"машина повернула {direction}")

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!!!")
        return self.speed


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!!!")
        return self.speed


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town_car = TownCar(50, "красный", "Toyota")
town_car2 = TownCar(70, "чёрный", "Lada")
sport_car = TownCar(150, "белый", "Ferrari")
work_car = TownCar(30, "жёлтый", "Honda")
work_car2 = TownCar(50, "бежевый", "Mercedes")
police_car = TownCar(100, "синий", "Ford")

cars = [town_car, town_car2, sport_car, work_car, work_car2, police_car]

for car in cars:
    print(f"Скорость машины: {car.speed}, цвет машины: {car.color}, марка машины {car.name}, "
          f"машина {'полицейская' if car.is_police else 'не полицейская'}")
    car.go()
    car.turn("вправо")
    car.turn("влево")
    print(f"скорость машины: {car.show_speed()}")
    car.stop()
