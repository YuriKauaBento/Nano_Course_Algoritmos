soma = 1
sinal = -1

for i in range(2, 201, 2):
    soma += sinal * (1 /i)

    sinal *= -1

print(f"{soma:.2f}")