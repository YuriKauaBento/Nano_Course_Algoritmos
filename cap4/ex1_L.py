n = int(input("Digite um número: "))
temp = 0
sequencia = []
a = 0
b = 1

while a <= n:
    sequencia.append(a)
    temp = a
    a = b
    b = temp + b

print(sequencia)