q = input()
w = input()
e = input()

a = len(q)
b = len(w)
c = len(e)


if a > b and a > c and c < b:
    print(e)
    print(q)
elif a > b and a > c and c > b:
    print(w)
    print(q)

elif b > a and b > c and c < a:
    print(e)
    print(w)
elif b > a and b > c and c > a:
    print(q)
    print(w)
elif c > a and c > b and a > b:
    print(w)
    print(e)
elif c > a and c > b and a < b:
    print(q)
    print(e)
