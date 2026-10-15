try:
    n = int(input("Digite um número inteiro: "))

    for i in range(1, 11):
        a = i * n
        print(f"{i} X {n} = {a}")
except ValueError:
    print("Erro! O número digitado deve ser inteiro.")