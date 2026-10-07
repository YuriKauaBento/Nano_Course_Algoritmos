try:
    n = int(input("Digite um número: "))
    fat = 1

    for i in range(1, n+1):
        fat *= i

    print(f"O fatorial de {n} é {fat}")
except ValueError:
    print("Erro! Digite um número inteiro.")