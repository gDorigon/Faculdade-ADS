import random

while True: 

    pontosJogador = 0
    pontosMaquina = 0

    while pontosJogador < 3 and pontosMaquina < 3:

        while True:
            jogador = int(input("digite: \n 1 para tesoura \n 2 para papel \n 3 para pedra \nR: "))
            if jogador in [1, 2, 3]:
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

        maquina = random.randint(1, 3)

        opcoes = {1: "tesoura", 2: "papel", 3: "pedra"}
        print(f"Escolha da maquina foi: {opcoes[maquina]}")

        if maquina == jogador:
            print("empate")

        elif (maquina == 1 and jogador == 2) or \
             (maquina == 2 and jogador == 3) or \
             (maquina == 3 and jogador == 1):
            print("a maquina venceu")
            pontosMaquina += 1

        else:
            print("o jogador venceu")
            pontosJogador += 1

        print(f"\nplacar:\nJogador: {pontosJogador}\nMaquina: {pontosMaquina}")
        print("-----------------------------------")

    if pontosJogador == 3:
        print("Parabéns, você venceu a partida!")
    else:
        print("A máquina venceu a partida.")

    resposta = input("\nQuer jogar novamente (S/N): ")
    if resposta.upper() != "S":
        print("Obrigado por jogar!")
        break
        