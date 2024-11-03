mouth=int(input("Введите номер месяяца "))

def month_to_season(mouth):
    if mouth == 12 or mouth == 1 or mouth == 2:
            print("Зима")
    elif mouth == 3 or mouth == 4 or mouth == 5:
            print("Весна")
    elif mouth == 6 or mouth == 7 or mouth == 8:
            print("Лето")
    else:
            print("Осень")



month_to_season(mouth)