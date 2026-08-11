#Trabalho Segunda 26/05
#João Aranda
#Caio Rodrigues
#Pedro Spagolla
#Miguel Reis

import random


#FUNÇÃO EXIBIR CABEÇALHO
print('''=================Bem-vindo ao jogo de adivinhação=================\n
                        REGRAS DO JOGO\n
Você tentara adivinhar um numero conforme as dicas passadas,\nira ter apenas 5 tentativas e irei te dizer se está chegando perto ou não.
''')


#FUNÇÃO PARA ESCOLHA DO NÚMERO SECRETO
def numero_secreto(minimo, maximo):
    numero = random.randint(minimo, maximo)
    return numero
print("Número secreto escolhido")


#ESCOLHA DO NÚMERO DO USUÁRIO 
def palpite_usuario():
    while True:
        palpite = input("Qual seu palpite de 1 a 20: ")

        if palpite.isdigit():
            return int(palpite)
            break
        else:
            print("Digite apenas números.")
            
        
numero_escolhido = palpite_usuario()
print(f"Você escolheu o número: {numero_escolhido}")


#IDENTIFICADOR DE RESPOSTAS DO USUÁRIO 
def verifica_numero(palpite_usuario, numero_secreto ):
    if numero_secreto > palpite_usuario:
        print("O número escolhido é maior que o sorteado.")

    elif palpite_usuario < numero_secreto:
        print("O número escolhido é menor que o sorteado.")

    else:
        print("Você acertou o número!")


while True:
    numero_secreto(1, 20)
    numero = palpite_usuario()
    verifica_numero(numero_secreto, numero)