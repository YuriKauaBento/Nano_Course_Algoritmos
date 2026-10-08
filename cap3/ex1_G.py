maior = 0
menor = 0
par = []
impar = []
posi = []
neg = []
cont = []
soma = 0
prod = 1

try:
    while True:
        n = int(input("Digite um número inteiro: "))

        if menor == 0 or menor > n:
            menor = n
        elif maior < n:
            maior = n

        if n % 2 == 0 or n == 0:
            par.append(n)
        else:
            impar.append(n)

        if n > 0:
            posi.append(n)
        elif n < 0:
            neg.append(n)

        soma += n
        prod *= n
        cont.append(n)

        op = input("Quer continuar?[S]/[N]: ").strip().upper()
        if op in 'SN':
            if op == 'N':
                break
        else:
            print("Opção inválida!")
except ValueError:
    print("Erro! O valor inserido deve ser um número inteiro!")
    
media = soma / len(cont)

print(f"Menor: {menor}")
print(f"Maior: {maior}")
print(f"Pares: {par}")
print(f"Impares: {impar}")
print(f"Positivos: {posi}")
print(f"Negativos: {neg}")
print(f"Somatória: {soma}")
print(f"Produtória: {prod}")
print(f"Média: {media}")
