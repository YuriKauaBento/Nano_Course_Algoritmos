try:
    n = int(input("Digite um número inteiro: "))

    for i in range(2, (n//2)+1):
        if n % i == 0:
            print(f"O número {n} não é primo!")
            break
        if i == n//2:
            print(f"O número {n} é primo!")
except ValueError:
    print("Erro! O valor inserido deve ser um número inteiro!")