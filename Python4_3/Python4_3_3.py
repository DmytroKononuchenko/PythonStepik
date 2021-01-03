a, b, c = int(input()), int(input()), int(input())

if c < a < b or b < a < c:
    print(a)
elif a < b < c or c < b < a:
    print(b)
else: print(c)