try:
    potencia_lampada = float(input("Digite a potência da lâmpada (em watts): "))
    largura = float(input("Digite a largura do cômodo (em metros): "))
    comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

    if potencia_lampada <= 0 or largura <= 0 or comprimento <= 0:
        print("Os valores devem ser maiores que zero.")
    else:
        area = largura * comprimento
        potencia_necessaria = area * 3
        qtd_lampadas = potencia_necessaria / potencia_lampada
        bocais = area / 3

        print(f"Área do cômodo: {area:.2f} m²")
        print(f"Número de lâmpadas necessárias (pela potência): {qtd_lampadas:.2f}")
        print(f"Quantidade de bocais disponíveis (1 a cada 3m²): {bocais:.2f}")
except ValueError:
    print("Entrada inválida. Por favor, digite valores numéricos.")