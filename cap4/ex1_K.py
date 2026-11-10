soma = 0
intervalo = []
total = []

while True:
    try:
        n = int(input("Digite um número inteiro: "))
        total.append(n)
        op = input("Quer continuar?[S/N]").strip().upper()

        while op not in 'SN':
            print("Erro! Opção inválida.")
            op = input("Quer continuar?[S/N]").strip().upper()

        if op == 'N':
            break
    except ValueError:
        print("Erro! Digite apenas números inteiros.")

for i in total:
    if 4 <= i <= max(total) and (i - 4) % 3 == 0:
        intervalo.append(i)
        soma += i

print(f"A soma do intervalo válido {intervalo} é de {soma}")
