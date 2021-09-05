#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_dict = {'One': 'Odin', 'Two': 'Dva', 'Three': 'Tri', 'Four': 'Cetire'}
my_f = open("my_file_task_4.txt", "r")
output_file = open("my_file_task_4_output.txt", "w")
for line in my_f:
    word_list = line.split(" ")
    word_list[0] = rus_dict.get(word_list[0])
    output_file.writelines(word_list)

my_f.close()
output_file.close()
