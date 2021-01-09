q = int(input())
a = q % 2
if a != 0:
    print("YES")
elif q == 2 or q == 4:
    print("NO")
elif 6 <= q <= 20 and q % 2 ==0:
    print("YES")
elif q > 20 and q % 2 == 0:
    print("NO")
