import datetime

# Урок 1. Знакомство с Python
# 1.
name = "Alexei"
bdate = datetime.datetime(1980, 12, 24)
age = 41

print(f"My name is {name}")
print(f"I'm {age} years old")
print(f"I was born on {bdate} ")

yourName = input("what is your name")
print('Hi' + yourName)

yourWeight = input("how much do you weigh")
print(yourName + " your weight is " + yourWeight)

# Задание 2

seconds_str = input("enter some seconds")
seconds_int = int(seconds_str)
seconds = seconds_int % 60
minutes = seconds_int // 60
hours = minutes // 60
minutes = minutes % hours

print(f"{hours:02}:{minutes:02}:{seconds:02}")  # чч:мм:сс

# Задание 3

number_str = input("enter some single digit number")
number_int = int(number_str)
number_int += int(number_str + number_str)
number_int += int(number_str + number_str + number_str)
print(number_int)

# Задание 4

nat_number_str = input("enter some natural number")
nat_number_int = int(nat_number_str)
max_number = 0
while nat_number_int > 0:
    number_to_compare = nat_number_int % 10
    if number_to_compare > max_number:
        max_number = number_to_compare

    nat_number_int = nat_number_int // 10
    if nat_number_int == 0:
        break

print(f"max number is {max_number}")

# Задание 5

proceeds_str = input("enter company proceeds")
costs_str = input("enter company costs")
proceeds_int = int(proceeds_str)
costs_int = int(costs_str)
if proceeds_int > costs_int:
    print("Profit")
    profit = proceeds_int - costs_int
    profitability = profit / proceeds_int
    print(f"profitability is {profitability}")
    employee_count_str = input("enter the number of employees")
    profit_per_employee = profit / int(employee_count_str)
    print(f"profit per employee is {profit_per_employee}")

elif proceeds_int < costs_int:
    print("loss")
else:
    print("loss equal to Profit")

# Задание 6

a_str = input("enter 1st day kilometers (a)")
b_str = input("enter total kilometers (b)")
a = int(a_str)
b = int(b_str)
days = 1
while a < b:
    print(f"{days}-й день: {round(a, 2)}")
    a *= 1.1
    days += 1

print(f"{days}-й день: {round(a, 2)}")
print(f"на {days}-й день спортсмен достиг результата — не менее {b} км.")
