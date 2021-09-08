#Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'zapusk otrisovki {self.title}')

class Pen(Stationary):

    def draw(self):
        print(f'zapusk otrisovki {self.title} Pen obj')

class Pencil(Stationary):

    def draw(self):
        print(f'zapusk otrisovki {self.title} Pencil obj')

class Handle(Stationary):

    def draw(self):
        print(f'zapusk otrisovki {self.title} Handle obj')

pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')
pen.draw()
pencil.draw()
handle.draw()
