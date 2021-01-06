a, b, a1, b1 = int(input()), int(input()), int(input()), int(input())

q = max(a, a1)
w = min(b, b1)

if q < w:
    print(a, b)
elif q == w:
    print(q)
else:
    print("пустое множество")
