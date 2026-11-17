
print("####################### CATEGORIAS ########################")

categorias = ["Massas", "Bebidas", "Petiscos", "Doces", "Salgados", "Pizza", "Churrasco", "Lanches", "Comida Japonesa", "Pastel"]

print(categorias)

pergunta = input("Escolha uma das categorias acima:")

match pergunta:
    case "Massas":
        print("Dia das Massas, com rodízio e descontos é toda quarta-feira!!")
    case "Bebidas":
        print("Dia das Bebidas, é todo dia!!")
    case "Petiscos":
        print("Dia dos Petiscos, que anda junto com as Bebidas!!")
    case "Doces":
        print("Dia das Doces, de amarga já chega a vida!!")
    case "Salgados":
        print("Dia das Salgados, de forno ou fritos são uma boa pedida!!")
    case "Pizza":
        print("Dia das Pizza, com rodízio e descontos é toda sexta-feira!!")
    case "Churrasco":
        print("Dia das Churrasco, não tem pra ninguém!!")
    case "Lanches":
        print("Dia das Lanches, rápido com qualidade!!")
    case "Comida Japonesa":
        print("Dia das Comida Japonesa, sofisticado que só!!")
    case "Pastel":
        print("Dia das Pastel, quem resiste?!")
    case _:
        print("Categoria não encontrada!")

