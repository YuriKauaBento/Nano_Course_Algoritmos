a = [1, 2 , 3, 4, 10, 30]
b = [7, 1, 2, 20, 3, 5, 10, 24, 2]
c = []
menor = 0
soma = 0
maior = None

if len(a) <= len(b):
    menor = len(a)
    maior = b
else:
    menor = len(b)
    maior = a

for i in range(0, menor):
    soma = a[i] - b[i]
    c.append(soma)

for i in range(menor, len(maior)):
    c.append(maior[i])

print(c)