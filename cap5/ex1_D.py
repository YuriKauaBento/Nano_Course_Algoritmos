c = 2
lista = [1]
for i in range(0, 99):
    lista.append(c)
    c += lista[i]

print(lista)