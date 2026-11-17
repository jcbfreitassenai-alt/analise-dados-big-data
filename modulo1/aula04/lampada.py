'''

Cálculo de Lâmpadas: 
Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para 
iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da 
lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do 
cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada 
3m² existe um bocal para uma lâmpada. 

'''

metro = 3
watts = 3
dimensoes = int(input("Insira a quantidade de metros quadrados do cômodo a ser iluminado: "))

calculo = int((dimensoes/metro)) 


print("A quantidade de lâmpadas para iluminar este cômodo é de: ", calculo)










