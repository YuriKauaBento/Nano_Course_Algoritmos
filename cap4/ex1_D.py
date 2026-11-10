try:
    n = int(input("Digite um número maior que 3: "))

    for i in range(3, n+1):
        num = i * (i-1) * (i-2)
        if num > n:
            print(f"{n} não é um número triangular!")
            break
        elif num == n:
            print(f"{n} é um número triangular!")
            break
except ValueError:
    print("Erro! O valor inserido deve ser um número inteiro!")
    