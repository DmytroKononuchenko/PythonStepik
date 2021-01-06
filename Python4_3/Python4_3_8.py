q = int(input())
if q < 0 or q >= 37:
    print("ошибка ввода")
elif q == 0:
    print("зеленый")

elif 1 <= q <= 10 or 19 <= q <= 28:
    if q % 2 == 0:
        print("черный")
    elif q % 2 != 0:
        print("красный")


elif 11 <= q <= 18 or 29 <= q <= 36:
    if q % 2 != 0:
        print("черный")
    elif q % 2 == 0:
        print("красный")
