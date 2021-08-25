#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, surname, bdate, sity, phone):
    print(f"Name: {name}, Surname: {surname}, Bdate: {bdate}, Sity: {sity}, Phone: {phone}")

name = input("input name: ")
surname = input("input surname: ")
bdate = input("input bdate: ")
sity = input("input location sity: ")
phone = input("input phone num: ")

user_info(
    name=name,
    surname=surname,
    bdate=bdate,
    sity=sity,
    phone=phone
)