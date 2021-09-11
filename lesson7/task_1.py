#  Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:

    def __init__(self, list):
        self.matrix = list

    def __str__(self):
        string = ''
        for i in self.matrix:
            for j in i:
                string += str(j) + '\t'
            string += '\n'
        return string

    def __add__(self, other):
        result_list = []
        for i in range(len(self.matrix)):
            result_list_element = []
            for j in range(len(self.matrix[0])):
                result_list_element.append(self.matrix[i][j] + other.matrix[i][j])
            result_list.append(result_list_element)
        result_matrix = Matrix(result_list)
        return (result_matrix)

my_matrix1 = Matrix([[1,2,3],[9,2,3],[1,2,3]])
my_matrix2 = Matrix([[2,2,2],[2,2,2],[1,2,3]])
print(my_matrix1)
print(my_matrix2)
result_matrix = my_matrix1+my_matrix2
print(result_matrix)
