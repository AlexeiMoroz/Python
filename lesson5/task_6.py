#Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
#Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

def count_sum_from_list(list_with_nums):
    total = 0
    num = ''
    for list_mem in list_with_nums:
        for char in list_mem:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                    total += (int(num))
                    num = ''
    return total

my_dict = {}
my_f = open("my_file_task_6.txt", "r")
for line in my_f:
    word_list = line.split(" ")
    if word_list[0] == '\n':
        continue
    my_dict[word_list[0]] = count_sum_from_list(word_list)

my_f.close()
print(my_dict)
