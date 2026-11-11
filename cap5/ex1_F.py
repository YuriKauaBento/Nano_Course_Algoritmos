try:
    n = 0
    pares = []
    impares = []

    for i in range(0, 100):
        op = ""
        n = int(input("Digite um número inteiro: "))

        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
        op = input("Quer continuar? [S]/[N]").strip().upper()

        if op == "N":
            break

    print(f"Números ímpares {impares}")
    print(f"Números pares {pares}")
except ValueError:
    print("ERRO! o valor inserido deve ser um número inteiro.")