try:
    lista = []
    menor = []
    maior = []
    for i in range(0, 3):
        n = int(input("Digite um número inteiro: "))
        lista.append(n)

    lista.sort()

    menor.append(lista[0:2])
    maior.append(lista[1:3])

    print(menor)
    print(maior)
except ValueError:
    print("O valor informado deve ser um número inteiro!")