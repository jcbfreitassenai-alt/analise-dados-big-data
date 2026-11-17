## FUNÇÕES:

def menu_inicial():

    print("*"*40)
    print("##### ATENDIMENTO LÁITCHI #####")
    print("*"*40)
    print("Para iniciarmos o atendimento, por favor digite seu nome e CPF: ")
    nome_user = input("Nome: ")
    id_user = input("CPF: ")
    print(f"Olá, {nome_user}! Seu identificador informado é {id_user}!")

inicio_sistema = menu_inicial()

inicio_sistema