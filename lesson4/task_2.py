#Представлен список чисел.
#Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

from random import randint

def generate_list(list_len):
    source_list = []
    for i in range(list_len):
        source_list.append(randint(0, 101))
    return source_list

list_len = 13
source_list = generate_list(list_len)
print(source_list)
generator = [el for ind,el in enumerate(source_list) if ind>1 and el>source_list[ind-1]]
print(generator)