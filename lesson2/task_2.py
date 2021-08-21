#Для списка реализовать обмен значений соседних элементов.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
#При нечётном количестве элементов последний сохранить на своём месте.
#Для заполнения списка элементов нужно использовать функцию input().

el_list = list()
i = 0
while i < 5:
    new_el = input("input next element of list")
    el_list.append(new_el)
    i += 1

print(el_list)

for el in el_list:
    el_index = el_list.index(el)
    if el_index == len(el_list)-1:
        break
    elif el_index % 2 == 0:
        el_list[el_index], el_list[el_index + 1] = el_list[el_index + 1], el_list[el_index]
        continue

print(el_list)
