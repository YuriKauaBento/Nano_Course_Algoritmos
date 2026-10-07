print("Calcule o valor final da mensalidade!")
while True:
    try:
        idade = int(input("Informe sua idade: "))
        base = float(input("Informe o valor base da mensalidade: "))

        while idade < 17 or idade > 70:
            print("Idade inválida!")
            idade = int(input("Informe sua idade: "))
        break
    except ValueError:
        print("Erro! Os valores de idade e mensalidade devem ser números.")


sexo = input("Informe seu sexo [F]/[M]: ").strip().upper()

while sexo not in 'FM':
    print("Sexo inválido!")
    sexo = input("Informe seu sexo [F]/[M]: ").strip().upper()

mod = None
final = None
risco = None

if sexo == 'F':
    mod = 0.8
else:
    mod = 1

if idade >= 17 and idade <= 20:
    risco = 1
elif idade >= 21 and idade <=24:
    risco = 2
elif idade >= 25 and idade <= 34:
    risco = 3
elif idade >= 35 and idade <= 64:
    risco = 4
elif idade >= 65 and idade <= 70:
    risco = 7

final = base * risco * mod

print(f"O valor da mensalidade final é de R$ {final:.2f}")