# Aula 5 - Desafio 1: Média escolar para 10 estudantes (for)
for i in range(10):
    print(f"Aluno {i + 1} de 10:")
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
    print(f"Média: {media}")

    if media >= 6.0:
        print("Aprovado\n")
    elif media < 3.0:
        print("Reprovado\n")
    else:
        print("Recuperação\n")
