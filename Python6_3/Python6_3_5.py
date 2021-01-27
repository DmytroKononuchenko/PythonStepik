a = len(input())
b = len(input())
c = len(input())

q = (2 * b - c - a) * (2 * c - b - a) * (2 * a - b - c)
if q == 0:
    print("YES")
else:
    print("NO")
