a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

o = []

while len(o) < 3:
    if a not in o:
        o.append(a)
    elif b not in o:
        if b < a:
            o.insert(0, b)
        else:
            o.append(b)
    elif c not in o:
        if c < o[0]:
            o.insert(0, c)
        elif c < o[1]:
            o.insert(1, c)
        else:
            o.append(c)


print(o)