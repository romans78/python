import time


class TrafficLight:
    def __init__(self):
        self.__color = None

    def running(self):
        colors_seconds = [("красный", 7), ("жёлтый", 2), ("зелёный", 5)]
        for color, seconds in colors_seconds:
            self.__color = color
            print(f"Загорелся {self.__color} свет")
            counter = seconds
            for t in range(seconds):
                print(f"Осталось {counter} секунд", end="")
                time.sleep(1)
                print("\r", end="")
                counter -= 1
            print(f"Потух {self.__color} свет\n")


traffic_light = TrafficLight()

for i in range(3):
    traffic_light.running()
