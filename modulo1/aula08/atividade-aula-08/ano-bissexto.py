
def eh_bissexto(ano):

    if ano % 400 == 0:
        return True

    elif ano % 100 == 0:
        return False

    elif ano % 4 == 0:
        return True

    else:
        return False


ano = int(input("Digite um ano: "))

if eh_bissexto(ano):
    print(f"O ano {ano} É bissexto.")
else:
    print(f"O ano {ano} NÃO é bissexto.")
