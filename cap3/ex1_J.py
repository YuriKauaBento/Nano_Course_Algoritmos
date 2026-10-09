try:
    n = int(input('blabla'))

    for i in range(n+1, 101):
        c = []

        for p in range(i, 0, -1):
            if i % p == 0 and n % p == 0:
                c.append(p)

        if len(c) == 1 and c[0] == 1:
            print(f"{n} e {i} são primos entre si!")
except ValueError:
    print("Erro! Digite apenas NÚMEROS INTEIROS!")
