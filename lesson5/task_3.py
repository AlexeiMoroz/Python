#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#Выполнить подсчет средней величины дохода сотрудников.

my_f = open("my_file_task_3.txt", "r")
line_count = 0
employe_list = []
total_sum = 0
for line in my_f:
    salary_info = line.split(" ")
    if float(salary_info[1]) < 20000:
        employe_list.append(salary_info[0])
    total_sum += float(salary_info[1])
    line_count += 1

print(f"Employes with salary < 20000 : {employe_list}")
print(f"Average salary : {total_sum/line_count}")
my_f.close()
