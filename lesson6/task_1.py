#Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод

from time import sleep
from itertools import cycle

class TrafficLight:
    __color = {'RED':7, 'YELLOW':2 , 'GREEN':3}

    def running(self):
        for el in cycle(TrafficLight.__color):
            print(el)
            sleep(TrafficLight.__color[el])

traficLight = TrafficLight()
traficLight.running()
