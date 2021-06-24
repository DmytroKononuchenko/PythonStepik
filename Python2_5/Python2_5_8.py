q = int(input())
a = q // 100
b = (q // 10) % 10
c = q % 10
print(q)
print(a, c, b, sep='')
print(b, a, c, sep='')
print(b, c, a, sep='')
print(c, a, b, sep='')
print(c, b, a, sep='')
