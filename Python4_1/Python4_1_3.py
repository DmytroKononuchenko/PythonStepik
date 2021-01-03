q = int(input())
a = q // 1000
b = (q - (a * 1000)) // 100
c = ((q - (a * 1000)) - b * 100) // 10
d = (((q - (a * 1000)) - b * 100) - c * 10) // 1

if a + d == b - c:
    print("ДА")
else: print("НЕТ")