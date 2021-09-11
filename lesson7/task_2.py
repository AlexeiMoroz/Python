#Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.

from abc import ABC, abstractmethod

class Clothes(ABC):

    @abstractmethod
    def tissue_consumption(self):
        pass

class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def tissue_consumption(self):
        return self.size / 6.5 + 0.5

class Costume(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def tissue_consumption(self):
        return 2 * self.height + 0.3

coat = Coat(13)
print(f'amount of fabric for coat - {coat.tissue_consumption}')

costume = Costume(20)
print(f'amount of fabric for costume - {costume.tissue_consumption}')

total_area = 0
clothes = []
clothes.append(coat)
clothes.append(costume)
for el in clothes:
    total_area += el.tissue_consumption

print(f'total area is - {total_area}')


