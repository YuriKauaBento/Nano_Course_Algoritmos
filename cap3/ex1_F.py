try:
    quant = int(input("Informe a quantidade de números: "))
    cont = 0
    soma = 0

    while cont < quant:
        n = int(input("Digite um número inteiro: "))
        soma += n
        cont += 1

    print(soma)
except ValueError:
    print("Erro! Digite apenas NÚMEROS INTEIROS.")