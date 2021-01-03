a, b, c = int(input()), int(input()), int(input())

if a == b and a == c and b == c:
    print("Равносторонний")

elif (a == b ) or (b == c) or (c == a):
    print("Равнобедренный")

else:
    print("Разносторонний")
