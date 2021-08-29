#Реализовать формирование списка, используя функцию range() и возможности генератора.
#В список должны войти четные числа от 100 до 1000 (включая границы).
#Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

def generate_list():
    source_list = [el for el in range(100, 1001) if el % 2 == 0]
    return source_list

def multiply_nums(num1, num2):
    return num1 * num2

source_list = generate_list()
print(source_list)
print(reduce(multiply_nums, source_list))
