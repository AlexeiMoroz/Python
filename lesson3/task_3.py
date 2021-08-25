#Реализовать функцию my_func(), которая принимает три позиционных аргумента,
#и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    num_set = [num1, num2, num3]
    num_set.sort(reverse=True)
    print(f"Two max number sum is {num_set[0] + num_set[1]}")

num1 = int(input("input 1st number: "))
num2 = int(input("input 2nd number: "))
num3 = int(input("input 3rd number: "))

my_func(num1, num2, num3)