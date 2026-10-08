try:
    n = int(input("Digite um número maior que 3: "))
    tri = []

    for i in range(3, n+1):
        num = i * (i - 1) * (i - 2)
        tri.append(num)

    print(f"Grupo de números trianguláres ate {n}: {tri}")
except ValueError:
    print("Erro! O valor inserido deve ser um número inteiro")