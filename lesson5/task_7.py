#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные
# о фирме: название, форма собственности, выручка, издержки.
#Пример строки файла: firm_1   ООО   10000   5000.
#Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
#Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).

import json

my_f = open("my_file_task_7.txt", "r")
out_list = []
firm_dict = {}
profit_count = 0
profit_total = 0
average_profit = 0
for line in my_f:
    word_list = line.split(" ")
    print(word_list)
    if word_list[0] == '\n':
        continue
    profit = int(word_list[2]) - int(word_list[3])
    firm_dict[word_list[0]] = profit
    if profit > 0:
        profit_count += 1
        profit_total += profit

if profit_count > 0:
    average_profit = profit_total/profit_count

out_list.append(firm_dict)
out_list.append({"average_profit": average_profit})

with open("my_file_task_7.json", "w") as write_f:
    json.dump(out_list, write_f)

my_f.close()
