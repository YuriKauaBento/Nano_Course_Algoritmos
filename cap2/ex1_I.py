while True:
    try:
        num = int(input("Digite um número inteiro: "))

        if num > 0 and num % 2 == 0:
            print('0')
        elif num < 0 and num % 2 != 0:
            print('1')
        elif num == 0:
            print('2')
        else:
            print('3')
        break
    except ValueError:
        print("Erro! o valor deve ser um número inteiro.")