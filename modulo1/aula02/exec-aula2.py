# nota1 = int(input("Insira nota AV1: "))
# nota2 = int(input("Insira nota AV2: "))
# nota3 = int(input("Insira nota AV3: "))
# nota4 = int(input("Insira nota AV4: "))
# media = int((nota1 + nota2 + nota3 + nota4)/4)

# print("A média é ", media)

# nota1 = float(input("Insira nota AV1: "))
# nota2 = float(input("Insira nota AV2: "))
# nota3 = float(input("Insira nota AV3: "))
# nota4 = float(input("Insira nota AV4: "))
# media = float((nota1 + nota2 + nota3 + nota4)/4)

# print("A média é ", media)

# if media >= 7:
#     print("Aluno Aprovado!")
# elif media < 5:
#     print("Aluno Reprovado!")
# else:
#     print("Aluno em Recuperação!")


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 and numero1 > numero3 and numero2 > numero3:
    print(numero3, numero2, numero1)
elif numero2 > numero1 and numero2 > numero3 and numero3 > numero1:
    print(numero1, numero3, numero2)
elif numero3 > numero1 and numero3 > numero2 and numero2 < numero1:
    print(numero2, numero1, numero3)
else:
    print(numero1, numero2, numero3)