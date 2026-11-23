# Aula 4 - Desafio 3: Rendimento do Taxista
preco_combustivel = 6.15

km_inicial = float(input("Odômetro no início do dia (km): "))
km_final = float(input("Odômetro no final do dia (km): "))
litros = float(input("Litros de combustível gastos: "))
total_recebido = float(input("Valor total recebido dos passageiros (R$): "))

km_rodados = km_final - km_inicial
consumo = km_rodados / litros
gasto_combustivel = litros * preco_combustivel
lucro = total_recebido - gasto_combustivel

print(f"Consumo médio: {consumo} km/L")
print(f"Lucro líquido do dia: R$ {lucro}")
