a = int(input())
b = a % 4
c = a % 100
q = a % 400
if b < 1 and c >= 1 or q < 1:
    print("YES")
else:
    print("NO")