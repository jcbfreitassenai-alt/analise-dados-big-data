# Aula 4 - Desafio 4: Código de Origem do Produto
codigo = int(input("Digite o código de origem do produto: "))

match codigo:
    case 1:
        print("Sul")
    case 2:
        print("Norte")
    case 3:
        print("Leste")
    case 4:
        print("Oeste")
    case 5:
        print("Nordeste")
    case 6:
        print("Nordeste")
    case 7:
        print("Sudeste")
    case 8:
        print("Sudeste")
    case 9:
        print("Sudeste")
    case 10:
        print("Centro-Oeste")
    case 11:
        print("Noroeste")
    case _:
        print("Importado")
