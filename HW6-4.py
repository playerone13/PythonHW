class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f"Новая машина: {self.name} (Цвет {self.color}) машина полицейская - {self.is_police}")

    def go(self):
        print(f"{self.name}: машина поехала")

    def stop(self):
        print(f"{self.name}: машина остановилась")

    def turn(self):
        print(f"{self.name}: машина повернула {'налево' if direction == o else 'направо'}")

    def show_speed(self):
        print(f"{self.name}: скорость автомобиля - {self.speed}")

class Workcar(Car):

    def show_speed(self):
        return f"{self.name}: скорость автомобиля - {self.speed} - превышение скорости"\
            if self.spped > 40 else f"{self.name}: скорость автомобиля - {self.show_speed}"

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('ДПС', 'Белый', 80)
police_car.go()