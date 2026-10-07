try:
    n = int(input("Digite um número: "))
    soma = 0
    un = []

    for i in range(1, n+1):
        soma += i
        un.append(i)

    print(f"A soma dos 'n' primeiros números inteiros positivos de {n} é {soma} ->", end=' ')
    for i in range(0, len(un)):
        if i == 0:
            print(f"({un[i]} ", end='+ ')
        elif i == len(un)-1:
            print(f"{un[i]})")
        else:
            print(f"{un[i]} ", end='+ ')

except ValueError:
    print("Erro! Digite um número inteiro.")
    