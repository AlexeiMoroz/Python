#Пользователь вводит строку из нескольких слов, разделённых пробелами.
#Вывести каждое слово с новой строки. Строки нужно пронумеровать.
#Если слово длинное, выводить только первые 10 букв в слове.

words = input("input some words")
splitted_words = words.split()
strNum = 0
for el in splitted_words:
    strNum += 1
    print (f"{strNum}. {el[:10]}")