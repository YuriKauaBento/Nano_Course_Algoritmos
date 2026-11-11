lista = [14, 15, 12, 16, 13, 11]
n = len(lista)

for i in range(n-1):
    for j in range(n-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print(lista)