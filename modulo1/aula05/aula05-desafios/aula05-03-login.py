# Aula 5 - Desafio 3: Tentativa de Login e Senha
usuario_correto = "admin"
senha_correta = "123456"
tentativas = 3

while tentativas > 0:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break  # sai do loop ao acertar

    tentativas = tentativas - 1
    print(f"Usuário ou senha incorretos. Tentativas restantes: {tentativas}")

if tentativas == 0:
    print("Número de tentativas esgotado. Acesso bloqueado.")
