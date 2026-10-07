while True:
    try:
        a = int(input("Informe o primeiro número: \n"))
        b = int(input("Informe o primeiro número: \n"))
        if a < 0 and b < 0:
            raise ValueError
    except ValueError:
        print("Número inválido! Digite apenas números inteiros e positivos.")
        break


    if a % 2 == 0 and b % 2 == 0:
        print("Par")
    elif a % 2 != 0 and b % 2 != 0:
        print("Impar")
    else:
        print("Outro")
    break