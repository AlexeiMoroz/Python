#—оздать список и заполнить его элементами различных типов данных.
#–еализовать скрипт проверки типа данных каждого элемента.
#»спользовать функцию type() дл€ проверки типа.
#Ёлементы списка можно не запрашивать у пользовател€, а указать €вно, в программе.

a_list = [1, 2.2, "Python", False, ['inner_list', 3], {1, 3, 5}, {"1": "January", "2": "February"}]
for el in a_list:
    if (type(el) == int):
        print(f"{el} - This is int")
    elif (type(el) == str):
        print(f"{el} - This is string")
    elif (type(el) == bool):
        print(f"{el} - This is bool")
    elif (type(el) == list):
        print(f"{el} - This is list")
    elif (type(el) == float):
        print(f"{el} - This is float")
    elif (type(el) == set):
        print(f"{el} - This is set")
    elif (type(el) == dict):
        print(f"{el} - This is dict")
    else:
        print (type(el))

