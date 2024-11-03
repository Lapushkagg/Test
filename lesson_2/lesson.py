# password = 19

# if (password == 18):
#     print("ok")

# if (password > 18):
#     print("неверный пароль")

# print("финал")


# rate=input("Оцените работу оператора от 1 до 5: ")
# rate_as_nomber=int(rate)

# if(rate_as_nomber<1):
#     rate_as_nomber = 1

# if(rate_as_nomber>5):
#     rate_as_nomber = 5


# if(rate_as_nomber==1):
#     feedback = input("Что нам улучшить: ")
# elif rate_as_nomber==2:
#     feedback = input("Что нам что вам смутило: ")
# elif rate_as_nomber==3:
#     feedback = input("Как нам стать лучше: ")
# elif rate_as_nomber==4:
#     feedback = input("Что нам улучшить: ")
# else:
#     print("Спасибо за вашу похвалу")


# for x in range(0,10):
#     print(x)

    
# for x in range(1,21):
#     print("x= ", x, "x2= ", x*x)


# students = ["Александр", "Михаил", "Мария", "Ольга", "Кирилл"]

    
# for y in range(0, len(students)):
#     print(students[y])

# l=len(students)

# # print(students[0])
# # print(students[1])
# # print(students[2])
# # print(students[3])
# # print(students[4])

# for i in range(0, l):
#     print(students[i])

#     word ="Test"

# for s in word:
#     print(s)

# for studen in students:
#     print(studen)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for n in nums:
#     if(n%2==1):
#         print(n)


# user_login = "admin"
# user_pass = "Qwerty123456"

# login=input("Login: ")
# passw=input("Pass: ")

# if login==user_login and passw==user_pass:
#     print("Вход разрешен")
# else:
#     print("Закрыто")

# crit1 = "Красный"
# crit2 = "что-то"

# color=input("Login: ")
# feer=input("Pass: ")


# if (color == crit1) or (feer==crit2):
#     print("Купи!")
# else:
#     print("Не бери")

# employee_list = ["Jonh Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]

# print(employee_list[1] + ", " + employee_list[-2])

# def dev_by_three(num):
#     if num%3==0:
#         print("Да")
#     else:
#          print("Нет")

# num=int(input("Введите число "))

# dev_by_three(num)

# import math

# def min_boxes(items): 
#    print("Минимальное количество коробок:",math.ceil(items / 5))

# items=int(input("Введите количество предметов: "))
# min_boxes(items)
# n = int(input("Введите число:"))

# def check_divisibility(n):
#         for i in range(1, n + 1):
#            if i % 4 == 0:
#                 print(f"{i} - Делится и на 2, и на 4")
#            elif i % 2 == 0:
#                 print(f"{i} - Делится на 2, но не на 4")
#            else:
#                 print(i)


# check_divisibility(n)

# def quarter_of_year(month):
#     if 1 <= month <= 3:
#         return "I квартал"
#     elif 4 <= month <= 6:
#         return "II квартал"
#     elif 7 <= month <= 9:
#         return "III квартал"
#     elif 10 <= month <= 12:
#         return "IV квартал"
#     else:
#         return "Неверный номер месяца"

# try:
#     month = int(input("Введите номер месяца (1-12): "))
#     print(quarter_of_year(month)) 
# except ValueError:
#     print("Пожалуйста, введите целое число от 1 до 12.")


lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

result = [x for x in lst if x > 15 and x % 3 == 0]

print(result)