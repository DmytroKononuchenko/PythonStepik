q = int(input())
a = int(q / 100)
b = int((q - (a * 100)) / 10)
c = int((q - (a * 100)) % 10)
v = max(a, b, c)
z = min(a, b, c)
x = (a + b + c) - (v + z)
if v - z == x:
    print("Число интересное")
else:
    print("Число неинтересное")
