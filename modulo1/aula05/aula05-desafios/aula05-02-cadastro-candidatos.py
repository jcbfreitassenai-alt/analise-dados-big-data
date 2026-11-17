# Aula 5 - Desafio 2: Cadastro de Candidatos (12 pessoas)
ano_atual = 2026

for i in range(12):
    print(f"Candidato {i + 1} de 12:")
    ano_nascimento = int(input("Ano de nascimento: "))
    idade = ano_atual - ano_nascimento

    if idade < 18:
        # Menor de 18: não coleta os demais dados
        print("Candidato menor de 18 anos. Não pode participar.\n")
    else:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("E-mail: ")
        print(f"Candidato {nome} cadastrado com sucesso!\n")
