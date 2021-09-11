#Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cell:

    def __init__(self, cel_num):
        self.cel_num = cel_num

    def __add__(self, other):
        return self.cel_num + other.cel_num

    def __sub__(self, other):
        return self.cel_num - other.cel_num if self.cel_num > other.cel_num else print("cell difference is less than zero")

    def __mul__(self, other):
        result_cel = Cell(self.cel_num * other.cel_num)
        return result_cel

    def __truediv__(self, other):
        result_cel = Cell(self.cel_num / other.cel_num)
        return result_cel

    def make_order(self, cels_in_row):
        full_rows = self.cel_num//cels_in_row
        rest = self.cel_num%cels_in_row
        return ('*'*cels_in_row + '\n')*full_rows + '*'*rest

    def __str__(self):
        return f"The cell contains {self.cel_num} cellules"

cell_1 = Cell(26)
print(cell_1.cel_num)
cell_2 = Cell(13)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print((cell_1 * cell_2).make_order(23))
