n = int(input("Введите число:"))


def cfizz_buzz(n):
    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            print(f"{i} - FizzBuzz")
        elif i % 5 == 0:
            print(f"{i} - Buzz")
        elif i % 3 == 0:
            print(f"{i} - Fizz")
        else:
            print(i)


cfizz_buzz(n)