a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b:
    if b > c:
        print (a + b)
    else:
        print(a + c)
elif b > a:
    if a > c:
        print(b + a)
    else:
        print(b + c)
