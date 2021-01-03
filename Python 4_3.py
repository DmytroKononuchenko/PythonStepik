a, b = int(input()), int(input())
q = input()
if q != "/" and q != "*" and q != "+" and q != "-":
    print("Неверная операция")
elif q == "*":
    print(a * b)
elif q == "-":
    print(a - b)
elif q == "+":
    print(a + b)
elif q == "/" and b == 0:
    print("На ноль делить нельзя!")
elif q == "/" and b > 0:
    print(a / b)
