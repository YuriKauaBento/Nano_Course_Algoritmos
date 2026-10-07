while True:
    try:
        sub =  0
        a = int(input("Informe o primeiro valor: "))
        b = int(input("Informe o segundo valor: "))
        if a != b:
            if a > b:
                sub = a - b
            else:
                sub = b - a
            print(f"resultado = {sub}")
            break
        else:
            print("Erro! Impossivel fazer a subtração!")
    except ValueError:
        print("Digite um número inteiro!")
        
