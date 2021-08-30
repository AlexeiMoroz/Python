#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
#В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
#Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

def salary(hours, rate, premium):
    return hours * rate + premium

hours = int(argv[1])
rate = int(argv[2])
premium = int(argv[3])
empsalary = salary(hours, rate, premium)
print(f"Employees salary is {empsalary}")
