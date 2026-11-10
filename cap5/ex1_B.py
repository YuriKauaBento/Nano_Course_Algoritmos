try:
    lista = []
    while True:
        n = int(input("Digite um número inteiro: "))
        if n % 10 == 7 or n % 10 == 5:
            lista.append(n)

        op = input("Quer continuar? [S]/[N]").strip().upper()
        if op == 'N':
            break
    print(lista)
except ValueError:
    print("O valor inserido deve ser um número inteiro.")