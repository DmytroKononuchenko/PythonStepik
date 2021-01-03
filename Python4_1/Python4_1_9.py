a = int(input())
b = int(input())
c = int(input())

if a<0: #Специально используется такая конструкция с тремя if

    a=0

if b<0:

    b=0

if c<0:

    c=0

print(a+b+c)
if a < 0 and b < 0 and c < 0:
    print(0)