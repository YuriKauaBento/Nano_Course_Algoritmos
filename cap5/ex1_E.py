try:
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite outro número inteiro: "))
    menor = 0
    maior = 0
    c = 1
    d = 2
    e = 0
    sequencia = []

    if a > b:
        maior = a
        menor = b
    else:
        maior = b
        menor = a

    for i in range(1, maior):
        if c >= maior:
            break

        if c >= menor:
            sequencia.append(c)

        e = c
        c = d
        d = e + d

    print(sequencia)
except ValueError:
    print("ERRO! O valor inserido deve ser um número inteiro.")