selos_5 = None
selos_3 = None

while True:
    try:
        valor = int(input("Informe o valor cobrado: "))
        if valor < 8:
            raise TypeError

        for selos in range(valor // 5, -1, -1):
            resto = valor - (selos * 5)

            if resto % 3 == 0:
                selos_3 = resto // 3
                selos_5 = selos
        print(f"Selos de 5 centavos: {selos_5}")
        print(f"Selso de 3 centavos: {selos_3}")
        break
    except ValueError:
        print("Erro! O valor deve ser um número inteiro.")
    except TypeError:
        print("Erro! O valor deve ser maior que 8.")
