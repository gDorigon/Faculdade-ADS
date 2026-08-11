# Alunos
# Guilherme Dorigon - 47583029
# João Victor Linares de Jesus - 46957405
# Miguel Augusto Rivera Mendes - 48741337
# Renan Alves - 47668865
# Vinicius Azara - 47607602


# Programa de Controle de Fluxo e Coleções
# ENTREGA 2

import random

estoque = {
    "mouse":1000,
    "teclado":5000,
    "monitor":1100,
    "cabo":10000,
    "gabinete":200,
    "placa de vídeo":1000,
    "fonte":500,
    "cadeira gamer":300,
    "headset":150,
    "mesa digitalizadora":100,
    "caixa de som":1000,
    "impressora 3D":50,
    "pen-drive":5000,
    "webcan":100,
    "smartwatch":2000,
    "ps5":3000,
    "oculos vr":50,
        }

historico = []
# -------------------------------------------------------------------------------
# MENU INICIAL(Renan)
while True:
    print("--------------------------------------")
    print("Bem vindo ao sistema do almoxariofado.")
    print("0. Adicionar Produto")
    print("1. Consultar Estoque")
    print("2. Retirar Item")
    print("3. Ver Histórico")
    print("4. Sair e Sortear")
    print("--------------------------------------")
    user_response = input('Escolha uma opção: ')
#---------------------------------------------------------------------------------
# LÓGICA DE ADIÇÃO DE PRODUTO NO ESTOQUE (Guilherme)
    if(user_response == "0"):
        nomeProduto = input("Digite o nome do produto: ") # RECEBE NOME DO PRODUTO
        quantidadeProduto = int(input("Digite a quantidade do produto: ")) # RECEBE QUANTIDADE DO PRODUTO
        if nomeProduto in estoque:
            estoque[nomeProduto] += quantidadeProduto # VERIFICA SE O PRODUTO EXISTE NO ESTOQUE, SE EXISTIR, ADICIONA A QUANTIDADE INSERIDA
        else:
            estoque[nomeProduto] = quantidadeProduto # SE NAO EXISTIR, ADICIONA NO ESTOQUE
        print(f"{quantidadeProduto}x do produto: '{nomeProduto}'adicionados")

#---------------------------------------------------------------------------------
# CONSULTA DE ESTOQUE (Renan)
    elif(user_response == "1"):
        for item,quantity in estoque.items(): # Para cada item do estoque, loga o nome do item e a quantidade em estoque
            print(f'| {item}  : {quantity} |')
    # elif(user_response == "2"):
#----------------------------------------------------------------------------------
# RETIRADA DE ITENS DO ESTOQUE (Vinicius)        
    elif(user_response == "2"):
        nomeProduto = input("Digite o nome do produto: ")
        quantidadeProduto = int(input("Digite a quantidade do produto: "))
        if nomeProduto in estoque:#processo de Retirada de itens
            if quantidadeProduto <= estoque[nomeProduto]: # Verifica se a quantidade é menos ou igual a quantidade em estoque
                estoque[nomeProduto] -= quantidadeProduto #retira quantidade do produto
                historico.append(f"{quantidadeProduto}x '{nomeProduto}' retirado")
                print(f"{quantidadeProduto}x do produto: '{nomeProduto}'retirados")#Mostra os itens retirados
            else:
                print("Não é possivel retirar quantidade maior que o estoque")
        else:
            print("Produto não encontrado")
# -----------------------------------------------------------------------------------
# VISUALIZAÇÃO DO HISTÓRICO DE MOVIMENTAÇÕES (Miguel)
    elif(user_response == "3"):
        if not historico:
            print("Nenhuma retirada registrada ainda.")
        else:
            print("--- Histórico de Retiradas ---")
            for registro in historico: # para cada registro no histórico, loga o registro gravado
                print(registro) 
# -----------------------------------------------------------------------------------
# FINALIZAÇÃO E SORTEIO (Joao Victor)
    elif(user_response == "4"):
       sorteio = random.choice(historico) # Escolhe um numero aleatório do histórico 
       print(f"O ganhador foi: {sorteio}")
       print("saindo do programa...")
       break
    else:
        print('Opção inválida. Por favor, tente novamente.')

# FIM DO PROGRAMA