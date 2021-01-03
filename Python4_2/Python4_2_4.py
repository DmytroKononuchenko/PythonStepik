a = int(input())
b = a % 7
c = a % 17

if (a > 999 and a <=9999) and (b < 1 or c < 1):
    print("YES")
else: print("NO")