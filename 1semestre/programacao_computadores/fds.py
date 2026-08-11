# Atividade de Programação: Opção B (Jogo da Forca Educativo)
# Mecânica: Uma palavra secreta é sorteada da lista. O programa exibe os traços (_ _ _) e gerencia a lista de letras que o jogador já tentou, controlando o número de vidas

# Alunos
# Guilherme Dorigon - 47583029
# João Victor Linares de Jesus - 46957405
# Miguel Augusto Rivera Mendes - 48741337
# Renan Alves - 47668865
# Vinicius Azara - 47607602

import random

# VARIÁVEIS GLOBAIS

vitorias = 0
derrotas = 0

# INICIALIZAÇÃO DO ARRAY DE PALAVRAS
palavras = [ 
    'algoritmo',
    'compilador',
    'recurso',
    'variavel',
    'software',
    'banco',
    'programacao',
    'memoria',
    'processador',
    'internet',
    'servidor',
    'hardware',
    'python',
    'java',
    'debug',
    'interface',
    'database',
    'inteligencia',
    'robotica',
    'criptografia'
 ]

# DEFINIÇÃO DE FUNÇÕES

def exibir_menu(vitorias, derrotas): # EXIBIÇÃO DO MENU COM PLACAR 
    print('-' * 10)
    print(' -- PLACAR ')
    print(f' ---- Vitórias: {vitorias}')
    print(f' ---- Derrotas: {derrotas}')
    print('-' * 10)
    print('Escolha uma das opções abaixo')
    print('1. Jogar')
    print('2. Como jogar')
    print('3. Sair')
    print('-' * 10)
    print('\n')

def sorteia_palavra(palavras):
    # tamanho_array_palavras = len(palavras)
    numero_sortear = int(random.random() * len(palavras)) # Gera um número randómico entre 0 e o número de indexes dentro do array de palavras

    palavra_sorteada = palavras[numero_sortear] # Palavra sorteada é a palavra referente ao número sorteado
    # Ex: retornou 0, vai ser a primeira palavra do array

    return palavra_sorteada # retorna a palavra

def exibir_regras(): # LISTA REGRAS DO JOGO DA FORCA
    print('Regras do Jogo:')
    print('O sistema escolherá uma palavra educativa aleatória e o jogador precisará advinhá-la letra por letra.')
    print('Cada letra escolhida pelo jogador que estiver na palavra, revelará em quais casas elas se encontram.')
    print('Cada letra escolhida que não estiver na palavra, será computada como um ERRO.')
    print('Se o jogador conseguir completar a palvra antes de atingir 6 ERROS ele vencerá a rodada.')

def exibir_forca(palavra, historico_de_tentativas):# Função  que exibe '_' ou letras da palavra
    campo = []

    for indice in range(len(palavra)):# para cada letra da palavra
        if palavra[indice] in historico_de_tentativas: # se a eltra inserida for igual a letra no index da palavra: imprime a letra
            print(palavra[indice], end=" ")
        else: # se não, imprime um underline '_'
            print(' _ ', end=" ")

    print("\n") # quebra de linha 

def contar_letras_em_palavra(caracter, palavra): # Contador de letras da palavra
    contador = 0

    for letra in palavra:
        if letra == caracter:
            contador = contador + 1

    return contador

def exibir_tentativas(tentativas): # Exibe as letras já escolhidas
    print('Letras já escolhidas: ')
    for letra in tentativas:
        print(letra)

def exibir_tentativas_report(correct_letras, lenght_of_palavra, erros): # Exibição do numero de acertos e erros com base nas tentativas
        print(f'Acertos: {correct_letras}/{lenght_of_palavra}')
        print(f'Erros: {erros}/6')

def play(): # Função principal que chama todas outras
    palavra = sorteia_palavra(palavras)
    lenght_of_palavra= len(palavra)
    correct_letras = 0
    erros = 0
    forca_completa = True
    historico_de_tentativas = []

    while forca_completa:

        print('\n')
        print('-' * 10)
       
        print('Letras já escolhidas: ', end=" ")
        for letra in historico_de_tentativas:
            print(letra, end=" ")

        print('\n')
        exibir_tentativas_report(correct_letras, lenght_of_palavra, erros)
        exibir_forca(palavra, historico_de_tentativas)

        letra = input('Escolha uma letra: ')
        if letra in palavra and letra not in historico_de_tentativas:
            print('Letra correta!')
            correct_letras = correct_letras + contar_letras_em_palavra(letra, palavra)
        else:
            print('Letra incorreta')
            erros = erros + 1

        historico_de_tentativas.append(letra)

        if erros >= 6:
            print('\n')
            print('Você atingiu o limite de erros!')
            print(f'A palavra era: {palavra}')
            exibir_tentativas_report(correct_letras,lenght_of_palavra, erros)
            forca_completa = False
        if correct_letras == lenght_of_palavra:
            print('\n')
            print(palavra)
            print('Você encontrou todas as letras!')
            exibir_tentativas_report(correct_letras,lenght_of_palavra, erros)
            forca_completa = False



# FLUXO PRINCIPAL DO PROGRAMA

print('Bem vindo ao Jogo da Forca Educativo');

exibir_menu(vitorias, derrotas)
escolha = input('Escolha: ')

if escolha == "1":
    play()
elif escolha == "2":
    exibir_regras()
else:
    pass

# FIM DO PROGRAMA