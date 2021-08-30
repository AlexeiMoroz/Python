#Представлен список чисел. Определить элементы списка, не имеющие повторений.
#Сформировать итоговый массив чисел, соответствующих требованию.
#Элементы вывести в порядке их следования в исходном списке.
#Для выполнения задания обязательно использовать генератор.

def unik_val(source_list):
    source_list2 = source_list
    unik_list = []
    for el in source_list:
        counter = 0
        for el2 in source_list2:
            if el2 == el:
                counter += 1

        if counter == 1:
            yield (el)

source_list =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(f"source_list - {source_list}")
generator = unik_val(source_list)
print(f"result_list - {[el for el in generator]}")
