#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

def generate_list(list_len):
    source_list = []
    for i in range(list_len):
        source_list.append(randint(0, 101))
    return source_list

list_len = 10
source_list = generate_list(list_len)

with open("my_file_task_5.txt", "w") as file:
    for num in source_list:
        file.write(f"{num} ")

num_sum = 0
my_f = open("my_file_task_5.txt", "r")
for line in my_f:
    num_list = line.split(" ")
    for num in num_list:
        if(num) == "":  #последний элемент пустой (или символ переноса строки?)
            continue
        num_sum += int(num)

print(f"Total num sum is : {num_sum}")
