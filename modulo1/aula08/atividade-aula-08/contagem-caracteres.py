
def contar_caractere(texto, caractere_procurado):

    contador = 0

    texto = texto.lower()
    caractere_procurado = caractere_procurado.lower()

    for caractere in texto:
        if caractere == caractere_procurado:
            contador += 1

    return contador


frase = input("Digite uma frase: ")
letra = input("Digite a letra que deseja procurar: ")

quantidade = contar_caractere(frase, letra)

print(f"A letra '{letra}' aparece {quantidade} vezes na frase.")
