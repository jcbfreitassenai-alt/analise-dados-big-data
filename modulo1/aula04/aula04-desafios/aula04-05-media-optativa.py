# Aula 4 - Desafio 5: Média do Aluno com Optativa
nota1 = float(input("Nota da avaliação 1: "))
nota2 = float(input("Nota da avaliação 2: "))
optativa = float(input("Nota da optativa (-1 se não fez): "))

# Se fez a optativa, ela substitui a menor das duas notas
if optativa != -1:
    if nota1 < nota2:
        nota1 = optativa
    else:
        nota2 = optativa

media = (nota1 + nota2) / 2
print(f"Média do semestre: {media}")

if media >= 6.0:
    print("Aprovado")
elif media < 3.0:
    print("Reprovado")
else:
    print("Recuperação")
