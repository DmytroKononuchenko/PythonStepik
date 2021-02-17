m = int(input())
n = int(input())
for _ in range(m, n + 1):
    if _ % 17 == 0 or (_ % 3 == 0 and _ % 5 == 0) or _ % 10 == 9:
        print(_)
