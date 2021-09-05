#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.

with open("my_file_task_1.txt", "a") as file:
    while True:
        inp_str = input("enter string: ")
        if inp_str == "":
            break
        file.write(inp_str + "\n")
		