# Trabalho python 3 - 2026

# Trabalho escolhido: 

import random

def sorteia_palavra():
    palavras = ["guilherme", "vinicius", "renan", "miguel", "joao"] # Array de palavras

    # tamanho_array_palavras = len(palavras)
    numero_sortear = int(random.random() * len(palavras)) # Gera um número randómico entre 0 e o número de indexes dentro do array de palavras

    palavra_sorteada = palavras[numero_sortear] # Palavra sorteada é a palavra referente ao número sorteado
    # Ex: retornou 0, vai ser a primeira palavra do array

    return palavra_sorteada # retorna a palavra 

def menu_jogo():
    print("====================")
    print(" JOGO DA FORCA ")
    print("====================")

def mostra_palavra(palavra, letras_tentadas): # Função  que exibe '_' ou letras da palavra
    for letra in palavra: # para cada letra da palavra
        if letra in letras_tentadas: # se a eltra inserida for igual a letra no index da palavra: imprime a letra
            print(f"{letra} ", end="")
        else: # se não, imprime um underline '_'
            print("_ ", end="")

def pede_letra(letras_tentadas):
    while True:
        letra = input("\nDigite uma letra: ")
        if letra in letras_tentadas:
            print("Letra já informada, tente novamente!")
        else:
            return letra

def adiciona_historico(letra, letras_tentadas):
    letras_tentadas.append(letra)

def verifica_vida(letra, palavra,vida):
        print(f"Vida restante: {vida}")
        if letra in palavra:
            print(f"A letra: {letra} existe na palavra!")
        else:
            vida -= vida



def jogo():
    palavra = sorteia_palavra()
    vidas = 5
    letras_tentadas = []
    menu_jogo()

    print("A palavra tem", len(palavra), "letras")

    while vidas > 0:
        mostra_palavra(palavra, letras_tentadas)
        letra = pede_letra(letras_tentadas)
        adiciona_historico(letra, letras_tentadas)
        verifica_vida(letra, palavra, vidas)
        print("Letras tendadas:")
        for i in letras_tentadas:
            print(i)
        


jogo()