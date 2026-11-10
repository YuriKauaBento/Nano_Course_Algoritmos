for i in range(2, 101):
    for n in range(i + 1, 101):
        menor = i
        maior = n

        while maior % menor != 0:
            resto = maior % menor
            maior = menor
            menor = resto

        if menor == 1:
            print(f"({i}, {n})")
            