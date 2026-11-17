# REPETIÇÕES

# LAÇO FOR:

# for i in range(10):
#     print(i)

# LAÇO WHILE
    
# pergunta = input("Consulta concluída. Digite S para continuar ou N para sair: ")

# while pergunta == "S" or pergunta == "s":
#     pergunta = input("Consulta concluída. Digite S para continuar ou N para sair: ")

#     print("----- Programa concluído. Volte sempre!! -----")


# LAÇO DO WHILE
    
while True:
    print(" --- BEM-VINDO AO SIMULADOR RONALDINHO SOCCER 3000 ---")
    player01 = input("Digite seu nome de jogador: ")
    print(player01)
    player02 = input("Digite seu nome de jogador: ")
    print(player02)



    '''
Tentativa de Login e Senha
Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
para digitar a senha correta.

● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
● Dê ao usuário 3 tentativas para acertar a combinação.
● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
break para sair do loop.
● Se a senha estiver errada, informe o erro e diminua o número de tentativas
restantes.
● Se as tentativas acabarem, imprima uma mensagem de bloqueio
'''

login = "admin"
senha = 123456
templogin = input("Digite seu login: ")
tempsenha = input("Digite sua senha: ")
contador = 0
limite = 3

# print("Digite seu login: ")
# print("Digite sua senha: ")

while True:
    if contador <= limite:   
        print(templogin)
        print(tempsenha)
        if templogin <> login and tempsenha <> senha:
            contador = contador + 1
            print("Login ou Senha inválido! Tente novamente!")
        else:      
            print("Senha bem-vindo!")