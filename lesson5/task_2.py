#Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
#количества слов в каждой строке.

my_f = open("my_file_task_2.txt", "r")
line_count = 0
for line in my_f:
    word_list = line.split(" ")
    line_count += 1
    print(f"Number of words in line {line_count} is - {len(word_list)}")

my_f.close()
print(f"Total lines - {line_count}")
