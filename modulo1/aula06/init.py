# from teste001 import menu_inicial

# menu_inicial()


# from calculadora import soma_dois_numeros, subtrai_dois_numeros, multiplica_dois_numeros, divide_dois_numeros

import time
import random
import os
import sys

from calculadora import *


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

teste1 = soma_dois_numeros(numero1, numero2)
teste2 = subtrai_dois_numeros(numero1, numero2)
teste3 = multiplica_dois_numeros(numero1, numero2)
teste4 = divide_dois_numeros(numero1, numero2)

# print(teste1)
# print(teste2)
# print(teste3)
# print(teste4)

print(teste1,teste2,teste3,teste4)
