#Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y.
#Задание необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def my_func_symple(x, y):
    return x ** y

def my_func_recursion(x, y):
    if y == 0:
        return 1
    if y > 0:
        return x * my_func_recursion(x, y - 1)
    if y < 0:
        return x * my_func_recursion(x, -1 * y - 1)

def my_func_cycle(x, y):
    deg = x
    if y < 0:
        for i in range(-1*y - 1):
            deg *= x
        return 1 / deg
    elif y > 0:
        for i in range(y-1):
            deg *= x
        return deg
    else:
        return 1

x = float(input("input x: "))
y = int(input("input y: "))

result = my_func_symple(x, y);
print(f"symple method {result}")

if y < 0:
    result = 1 / my_func_recursion(x, y)
elif y > 0:
    result = my_func_recursion(x, y)

print(f"recursion method {result}")

result = my_func_cycle(x, y)
print(f"cycle method {result}")
