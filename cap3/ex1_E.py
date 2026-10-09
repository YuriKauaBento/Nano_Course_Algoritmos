try:
    n = int(input("Digite um número: "))
    c = 0

    for i in range(1, n+1):
        if n % i == 0:
            c += 1
        if c > 2:
            print(f"O número {n} não é primo!")
            break
    
    if c == 2:
        print(f"O número {n} é primo!")
except ValueError:
    print("Erro! O valor inserido deve ser um número intero.")