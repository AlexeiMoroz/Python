#Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
#Например, print(int_func(‘text’)) -> Text
def int_func(lower_text):
    first_letter = lower_text[0]
    return chr(ord(first_letter)-32) + lower_text[1:]

lowercaseWord = input("enter some word")
firstUpKey = int_func(lowercaseWord)
print(firstUpKey)
lowercaseWords = input("enter some splitted words")
splitted_words = lowercaseWords.split()
out_string = ""
for el in splitted_words:
    out_string = out_string + int_func(el) + " "
print(out_string)