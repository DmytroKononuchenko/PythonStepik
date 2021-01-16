from math import *

a = float(input())
b = float(input())
c = float(input())

d = (b ** 2) - (4 * a * c)
if d < 0:
    print("Нет корней")
elif d == 0:
    x = -b / (2 * a)
    print(x)
elif d > 0:
    x1 = (- b + sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    x2 = (- b - sqrt(((b ** 2) - (4 * a * c)))) / (2 * a)
    if x1 > x2:
        x1, x2 = x2, x1
        print(x1, x2, sep='\n')
