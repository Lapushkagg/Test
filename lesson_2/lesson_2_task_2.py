def is_year_leap(year):
    if year%4==0:
        print("год ",year,": True")
    else:
        print("год ",year,": False")


year=int(input("Проверка высокстного года "))

is_year_leap(year)