# Aula 4 - Desafio 2: Quantidade de Caixas de Azulejos
comprimento = float(input("Comprimento da cozinha (m): "))
largura = float(input("Largura da cozinha (m): "))
altura = float(input("Altura da cozinha (m): "))

# Quatro paredes: 2 de (comprimento x altura) e 2 de (largura x altura)
area_paredes = 2 * comprimento * altura + 2 * largura * altura

# Cada caixa cobre 1,5 m² (arredondado para cima)
caixas_exato = area_paredes / 1.5
caixas = float(caixas_exato)
if caixas < caixas_exato:
    caixas = caixas + 1

print(f"Área das paredes: {area_paredes} m²")
print(f"Caixas de azulejos necessárias: {caixas}")
