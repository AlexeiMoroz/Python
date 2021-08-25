#Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def divide_two_nums(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print('zerro division detected')

num1 = int(input("input first number"))
num2 = int(input("input second number"))
divide_two_nums(num1, num2)