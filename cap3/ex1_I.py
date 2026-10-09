n = 2
c = 0
primo = 0

while True:
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
        if c > 2:
            break
    if c == 2:
        print(n)

    c = 0
    n += 1
    if n == 100000:
        break
