
import random


def rolar_dado(lados):
    resultado = random.randint(1, lados)
    return resultado


print("SIMULADOR DE BATALHA")

input("\nPressione ENTER para rolar o Ataque (d20)...")
ataque = rolar_dado(20)

input("Pressione ENTER para rolar o Dano (d8)...")
dano = rolar_dado(8)

print("\n--- RESULTADO DA BATALHA ---")
print(f"Resultado do Ataque (d20): {ataque}")
print(f"Resultado do Dano (d8): {dano}")

print("\nSimulação finalizada!")
