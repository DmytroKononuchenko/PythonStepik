x1 = int(input())  # 1 - 8,
y1 = int(input())  # 18 - 88

x2 = int(input())  # 1 - 8
y2 = int(input())  # 18 - 88

a = x2 - x1
b = y2 - y1


if -1 <= y1 - y2 <= 1 and -1 <= x1 - x2 <= 1:
    print("YES")
else:
    print("NO")