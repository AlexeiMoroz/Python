#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Cообщить, к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и dict

month_list = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
month_dict = {"1": "January", "2": "February", "3": "March", "4": "April", "5": "May", "6": "June",
              "7": "July", "8": "August", "9": "September", "10": "October", "11": "November", "12": "December"}

mounth_number = input("input month number")
print(f"Month name is {month_list[int(mounth_number)-1]}  (""list method"")")
print(f"Month name is {month_dict[mounth_number]}  (""dict method"")")
