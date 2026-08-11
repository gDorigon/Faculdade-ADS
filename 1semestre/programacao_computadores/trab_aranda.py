
# Importa a biblioteca random para conseguir gerar números aleatórios
import random


# Função que mostra o menu inicial do jogo
def menu_inicial():
    # Apenas prints para deixar o menu organizado e bonito
    print(">==-- JOGO DE ADIVINHAR NÚMERO --==<\n")
    print(" 1 - Jogar no modo fácil ( 1 - 10 )")
    print(" 2 - Jogar no modo médio ( 1 - 100 )")
    print(" 3 - Jogar no modo difícil ( 1 - 1000 )")
    print(" 4 - Jogar no modo extremo ( 1 - 10.000 )")
    print(" 5 - Jogar modo customizado (escolha o limite)")
    print(">==------------------------------==<\n")


# Função responsável por perguntar a dificuldade do jogo
def escolha_modo_jogo():
    # Loop infinito para continuar perguntando até o usuário digitar certo
    while True:
        # Recebe o valor digitado pelo usuário
        escolha = input("Escolha uma opção para jogar: ")
        # Verifica se o usuário digitou apenas números
        if escolha.isdigit():
            # Converte o valor para inteiro antes de retornar
            return int(escolha)
        else:
            # Caso o usuário digite letras ou símbolos
            print("Digite apenas números inteiros.")


# Função usada caso o jogador escolha modo customizado
def limite_customizado():
    # Usuário escolhe até qual número o jogo pode ir
    limite = int(input("Informe o limite do jogo: "))
    # Gera um número aleatório entre 1 e o limite escolhido
    numero_final = random.randint(1, limite)
    # Retorna o número secreto gerado
    return numero_final

# Função que gera o número secreto dependendo da dificuldade escolhida
def gera_numero_pela_escolha(dificuldade):
    # Match case funciona parecido com switch case
    match dificuldade:
        # Fácil -> gera número entre 1 e 10
        case 1:
            numero_aleatorio = random.randint(1, 10)
        # Médio -> gera número entre 1 e 100
        case 2:
            numero_aleatorio = random.randint(1, 100)
        # Difícil -> gera número entre 1 e 1000
        case 3:
            numero_aleatorio = random.randint(1, 1000)
        # Extremo -> gera número entre 1 e 10000
        case 4:
            numero_aleatorio = random.randint(1, 10000)
        # Modo customizado chama outra função
        case 5:
            numero_aleatorio = limite_customizado()
        # Caso o usuário escolha uma opção inválida
        case _:
            print("Opção inválida! Escolhendo modo médio por padrão.")
            # Define automaticamente o modo médio
            numero_aleatorio = random.randint(1, 100)
    # Retorna o número secreto criado
    return numero_aleatorio


# Função que pede um chute para o jogador
def solicita_chuta():
    # Recebe o número digitado
    chute = int(input("Informe um número para adivinhar: "))
    # Retorna o chute
    return chute

# Função responsável por verificar se o jogador acertou o número
def verifica_numero(numero_aleatorio, numero_inserido):
    # Se o número digitado for maior que o secreto
    if numero_inserido > numero_aleatorio:
        print(f"O número {numero_inserido} é maior que o número secreto.\n")
        # Retorna False porque o jogador ainda não acertou
        return False
    # Se o número digitado for menor que o secreto
    elif numero_inserido < numero_aleatorio:
        print(f"O número {numero_inserido} é menor que o número secreto.\n")
        # Também retorna False
        return False
    # Caso contrário significa que acertou
    else:
        print(f"Você acertou! O número secreto era: {numero_aleatorio}\n")
        # Retorna True para encerrar o jogo
        return True

# Função principal do jogo
def jogo():
    # Mostra o menu inicial
    menu_inicial()
    # Guarda a dificuldade escolhida pelo jogador
    dificuldade = escolha_modo_jogo()
    # Gera o número secreto baseado na dificuldade
    numero_secreto = gera_numero_pela_escolha(dificuldade)
    # Loop principal do jogo
    while True:
        # Pede um chute para o usuário
        chute = solicita_chuta()
        # Verifica se acertou o número secreto
        if verifica_numero(numero_secreto, chute):
            # Se acertou, encerra o loop e finaliza o jogo
            break

# Chama a função principal para iniciar o jogo
jogo()
