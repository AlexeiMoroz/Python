#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} started')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} is turned {direction}')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'TownCar {self.name} is over speed')
        else:
            print(f'TownCar {self.name} speed is normal')

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'WorkCar {self.name} is over speed')
        else:
            print(f'WorkCar {self.name} speed is normal')

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

town = TownCar(59, "Blue", "Wv Golf", False)
print(f'is police {town.is_police}')
print(town.show_speed())

work = WorkCar(50, "RED", "Toyota", False)
print(work.show_speed())

police = PoliceCar(79, "Blue", "Reno")
print(f'is police {police.is_police}')

sport = SportCar(150, "RED", "Lamba")
sport.go()
sport.show_speed()
sport.turn("LEFT")
sport.stop()
