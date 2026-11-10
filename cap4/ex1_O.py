try:
    n = int(input("Digite um número inteiro e posistivo: "))

    if n < 0:
        raise ValueError
    
    soma = 0
    a = 1

    for i in range(1, n+1):
        if i == n:
            print(a)
        else:
            print(a, end=", ")

        soma += a
        a *= 2

    print(f"A soma dos termos é de: {soma}")

except ValueError:
    print("Erro! O número digitado deve ser inteiro e positivo.")
