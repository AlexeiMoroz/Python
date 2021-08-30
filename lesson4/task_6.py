#Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее

from itertools import count, cycle

def generate_list(start, stop):
    source_list = []
    for el in count(start):
        if el > stop:
            break
        else:
            source_list.append(el)

    return source_list

def iterate_list(source_list, stop):
    с = 0
    for el in cycle(source_list):
        if с > stop:
            break
        print(el)
        с += 1

#а) итератор, генерирующий целые числа, начиная с указанного,
start_list = 3
stop_list = 10
source_list = generate_list(start_list, stop_list)
print(source_list)

#б) итератор, повторяющий элементы некоторого списка, определенного заранее
stop_iterations = 20
iterate_list(source_list, stop_iterations)
