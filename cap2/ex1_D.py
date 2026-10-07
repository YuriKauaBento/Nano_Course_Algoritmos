idade = int(input("Informe sua idade: "))
risco = input("Informe o risco: \n"
              "B - Baixo\n"
              "M - Médio\n"
              "A - Alto\n"
              ).strip().upper()
categoria = 0

if idade >= 17 and idade <= 20:
    if risco == "B":
        categoria = 1
    elif risco == "M":
        categoria = 2
    elif risco == "A":
        categoria = 3
elif idade >= 21 and idade <= 24:
    if risco == "B":
        categoria =  2
    elif risco == "M":
        categoria = 3
    elif risco == "A":
        categoria = 4
elif idade >= 25 and idade <= 34:
    if risco == "B":
        categoria = 3
    elif risco == "M":
        categoria = 4
    elif risco == "A":
        categoria = 5
elif idade >= 35 and idade <= 64:
    if risco == "B":
        categoria = 4
    elif risco == "M":
        categoria = 5
    elif risco == "A":
        categoria = 6
elif idade >= 65 and idade <= 70:
    if risco == "B":
        categoria = 7
    elif risco == "M":
        categoria = 8
    elif risco == "A":
        categoria = 9
else:
    print("Idade inválida!")


print(f"A categoria para seu seguro é {categoria}")