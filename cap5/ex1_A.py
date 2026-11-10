try:
    temp = []
    definitivo = []

    while True:
        n = int(input("Digite um número inteiro: "))
        temp.append(n)
        op = input("Quer continuar? [S]/[N]").strip().upper()
        if op == 'N':
            break

    media = sum(temp) / len(temp)

    for i in temp:
        if i > media:
            definitivo.append(i)

    print(definitivo)
except ValueError:
    print("ERRO! O valor informado deve ser um número inteiro!")