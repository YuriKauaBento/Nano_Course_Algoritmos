while True:
    try:
        num1 = int(input("Informe o primeiro valor: "))
        num2 = int(input("Informe o segundo valor:  "))
        num3 = int(input("Informe o terceiro valor: "))

        if num1 > num2 + num3:
            print('0')
        elif num1 == num2 or num1 == num3 or num2 == num3:
            print('1')
        elif num2 % 2 == 0:
            print('2')
        elif num1 % 2 != 0:
            print('3')
        else:
            print('4')
        break
    except ValueError:
        print("Erro! Os valores devem ser inteiros.")