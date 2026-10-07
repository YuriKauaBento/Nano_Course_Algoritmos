maior = 0
menor = 0
soma = 0

while True:
    try:
        a = int(input("Digite o primeiro valor: \n"))
        b = int(input("Digite o segundo valor: \n"))
        c = int(input("Digite o terceiro valor: \n"))
    except ValueError:
        print("Valor incorreto! Digite apenas valores positivos.")
        break

    lista =[a, b, c]
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
    
    maior = lista[n - 1]
    menor = lista[0]
    soma = maior - menor
    break

print(soma)
