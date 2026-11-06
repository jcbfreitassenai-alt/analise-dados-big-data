### CONTEXTO 1:

'''
PARA QUE EU POSSA DIRIGIR, EU PRECISO TER:
- DOCUMENTO (CNH) EM POSSE;
- MAIORIDADE (+18 ANOS);
- NÃO ESTAR ALCOOLIZADO. 
'''

pergunta1 = input("Você tem os documentos em mãos?")
pergunta2 = int(input("Qual a sua idade?"))
pergunta3 = input("Você consumiu bebida alcoólica antes de dirigir?")

if pergunta1 == "sim" and pergunta2 >= 18:
    print("Pode dirigir.")
elif pergunta1 == "sim" and pergunta3 == "sim":
    print("Não pode dirigir!")


# trem = input("Você veio de trem?")
# busao = input("Você veio de ônibus?")
# metro = input("Você veio de metrô?")

# if trem == "sim" or busao == "sim" or metro == "sim":
#     print("Bem-vindo(a) ao SENAC!!")
# else:
#     print("Tarifa dinâmica, né?! =( ")


