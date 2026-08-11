# Projeto Final (Entrega 4) da Disciplina de Programação de Computadores - Terça - 1ADS (2218215)

# Alunos:
# Renan Alves (RGM 47668865)
# Guilherme Dorigon (RGM 47583029)


# Enunciado:
# SISTEMA DE BLINDAGEM DE CADASTROS E TRANSAÇÕES. Você e sua equipe devem criar um sistema de software para automação de um dos cenários comerciais abaixo (escolha apenas um):
# 2. Sistema de Controle de Estoque e Vendas (Cadastro de produtos, quantidade, preço e movimentações)

# BASE DE DADOS (EM MEMÓRIA)
produtos = {
    "SKU001": {
        "nome": "Monitor Samsung Odyssey OLED G6",
        "preco": 8099.00,
        "quantidade": 10,
    },
    "SKU002": {
        "nome": "Monitor Samsung Odyssey OLED G5",
        "preco": 3299.00,
        "quantidade": 20,
    },
    "SKU003": {
        "nome": "Monitor Samsung ViewFinity S8",
        "preco": 8099.00,
        "quantidade": 10
    },
    "SKU004": {
        "nome": "Monitor Samsung ViewFinity S5",
        "preco": 8099.00,
        "quantidade": 10,
    },
    "SKU005": {
        "nome": "Monitor Sony INZONE M9",
        "preco": 3799.00,
        "quantidade": 40,
    },
    "SKU006": {
        "nome": "Monitor Sony INZONE M10S",
        "preco": 8699.00,
        "quantidade": 5,
    },
    "SKU007": {
        "nome": "Monitor Importado Premium Deluxe Sony BVM-HX3110",
        "preco": 399000.00,
        "quantidade": 1,
    },
    "SKU008": {
        "nome": "Monitor LG UltraGear 27gp850-b",
        "preco": 3799.00,
        "quantidade": 90,
    },
    "SKU009": {
        "nome": "Monitor LG DualUp 28MQ780-B",
        "preco": 3399.00,
        "quantidade": 120,
    },
}

movimentacoes = {
    "MV0001": {
        "tipo": "venda",
        "produto": "SKU009",
        "valor": 3399.00,
        "quantidade": 1,
    },
    "MV0002": {
        "tipo": "venda",
        "produto": "SKU009",
        "valor": 3300.00,
        "quantidade": 1,
    },
    "MV0003": {
        "tipo": "compra",
        "produto": "SKU009",
        "valor": 2100.00,
        "quantidade": 2,
    },
}


# FUNÇÕES (para ARQUITETURA MODULAR LIMPA)
def exibir_menu_inicial():
    print("-" * 15)
    print("| Bem vindo ao Sisetma de Controle e Estoque de Vendas")
    print("|")
    print("| Escolha uma das opções abaixo: ")
    print("|   1. Exibir saldo de estoque")
    print("|   2. Exibir relatório de vendas")
    print("|   3. Exibir relatório de compras")
    print("|   4. Cadastrar produto")
    print("|   5. Cadastrar pedido de venda")
    print("|   6. Cadastrar pedido de compra")
    print("|   7. Sair")
    print("-" * 15)


def exibir_estoque():
    print("-" * 15)
    print("|-| Exibindo saldo de estoque... ")
    for sku, detalhes in produtos.items():
        print(f"|--| {sku}")
        print(f"|----| Produto: {detalhes.get('nome')}")
        print(f"|----| Preço Unitário: {detalhes.get('preco')}")
        print(f"|----| Quantidade: {detalhes.get('quantidade')}")


def exibir_vendas():
    pass


def exibir_compras():
    pass


def listar_skus():
    for sku, detalhes in produtos.items():
        print(f"|----| {sku}: {detalhes.get('nome')}")


def cadastar_produto():
    print("-" * 15)
    print("|-| Cadastro de Produto")

    # Esse bloco faz a coleta dos dados referente ao produtoque vai ser cadastrado, iniciando pela coleta do SKU e fazendo a verificação se é um SKU que já está cadastrado.
    try: 
        sku = input("|-| Informe o SKU do produto: ")
        if sku in produtos:
            raise ValueError("Já existe um produto com este SKU.")
        nome = input("|-| Nome -> ")
        preco = float(input("|-| Preço -> "))
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        quantidade = int(input("|-| Quantidade -> "))
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
    except ValueError as erro:
        print(f"Erro: {erro}")

    # FInaliza o cadastro e salva o produto no bloco do else
    else:
        produtos[sku] = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade,
        }

        print("|-| Produto cadastrado com sucesso!")
    # finaliza operação
    finally:
        print("|-| Cadastro registrado no log.")

def cadastrar_venda():
    print("-" * 15)
    print("|-| Iniciando cadastro venda")
    print("|-| Informe o SKU do produto ou digite 'listar' para ver os SKUs disponíveis.")

    while True:
        sku_informado = input("|-| SKU -> ") # Solicita um SKU

        try:
            if sku_informado == "listar": # Caso o usuário digite "listar", exibe os SKUs disponíveis e solicita novamente o SKU
                listar_skus()
                continue

            produto = selecionar_produto_por_sku(sku_informado)

        except ValueError:
            print("|-| SKU inválido.") # Erro caso seja um SKu inválido
        else:
            print(f"|-| Produto {produto.get('nome')} encontrado!") # Exibe o nome do produto encontrado
            break

    print("|-| Informe a quantidade vendida.")

    while True:
        try:
            quantidade_venda = int(input("Quantidade -> "))

            if quantidade_venda <= 0:
                raise ValueError(
                    "A quantidade deve ser maior que zero." # Solicita uma quandidade de produtos vendidos
                )

            if quantidade_venda > produto.get("quantidade"):
                raise ValueError(
                    "Estoque insuficiente para realizar a venda." # trastativa caso seja uma quantidade inválida
                )

        except ValueError as erro: # Tratativa de erro para quantidade inválida
            print(f"Erro: {erro}")

        else:
            break

    valor_venda = produto.get("preco") # Atribui o valor da venda com base no preço do produto

    numero_da_movimentacao = len(movimentacoes) + 1
    id_da_movimentacao = "MV" + completar_zeros(numero_da_movimentacao) # REgistra log da venda e atribui ID da venda

    movimentacoes[id_da_movimentacao] = {
        "tipo": "venda",
        "produto": sku_informado,
        "valor": valor_venda,
        "quantidade": quantidade_venda,
    }
 # Registra log do produto vendido
    produtos[sku_informado]["quantidade"] = (
        produtos[sku_informado]["quantidade"] - quantidade_venda
    )

    print("|-| Venda registrada com sucesso!")

    print("|-| Operação registrada em log.") # Fim do bloco de venda 

def cadastrar_compra():
    # Exibindo submenu
    print("-" * 10)
    print("|-| Iniciando cadastro de pedido de compra com lançamento de estoque... ")

    # Colhendo a chave do dicionário e inicializando variaveis importantes
    print("|-| Por favor, informe o SKU do produto da compra.")
    print("|-| Caso você não se lembre do SKU, por favor digite 'listar'")

    # Selecionando o dicionário com informações do  produto
    while True:
        sku_informado = input("|-| SKU -> ")
        produto = {}

        try:
            if sku_informado == "listar":
                listar_skus()
                print("|-| Por favor, informe o SKU do produto da compra.")
                continue
            else:
                produto = selecionar_produto_por_sku(sku_informado)
        except ValueError:
            print(
                "O valor fornecido não é um número válido. Por favor, tente novamente."
            )
        else:
            nome_do_produto = produto.get("nome")
            print(f"|-| Produto {nome_do_produto} encontrado!")
            break

    # Atribuindo valor à compra
    print(
        "|-| Por favor, insira o valor unitário (preço de cada unidade do produto) da compra."
    )
    print(
        "|-| Caso o valor tenha decimais (centavos), por favor use o ponto (.) em vez da vírgula para separar as casas decimais."
    )
    valor_da_compra = coletar_input_numerico()

    # Atribuindo quantidade à compra
    print("|-| Por favor, informe quantas unidades foram compradas.")
    quantidade_da_compra = coletar_input_numerico()

    # Salvando movimentação
    numero_da_movimentacao = (
        len(movimentacoes) + 1
    )  # verificando qual será o próximo número... por exemplo, depois de MV0003 temos o número 4
    id_da_movimentacao = "MV" + completar_zeros(numero_da_movimentacao)

    print("|-| Valores a serem salvos: ")
    print(f"|--| ID da Movimentação: {id_da_movimentacao}")
    print(f"|--| SKU: {sku_informado}")
    print(f"|--| Valor: {valor_da_compra}")
    print(f"|--| Quantidade: {quantidade_da_compra}")
    movimentacoes[id_da_movimentacao] = {
        "tipo": "compra",
        "produto": sku_informado,
        "valor": valor_da_compra,
        "quantidade": quantidade_da_compra,
    }

    # Atualizando estoque
    produtos[sku_informado]["quantidade"] = (
        produtos[sku_informado]["quantidade"] + quantidade_da_compra
    )

    print("|--| Movimentação salva com sucesso! Estoque atualizado!")


def coletar_input_numerico():
    numero_fornecido = input("Valor -> ")

    while True:
        try:
            numero_convertido = float(numero_fornecido)
        except ValueError:
            print(
                "O valor fornecido não é um número válido. Por favor, tente novamente."
            )
        else:
            return numero_convertido


def selecionar_produto_por_sku(sku):
    produto = produtos.get(sku, {})
    if produto == {}:
        raise ValueError("SKU não corresponde a um produto cadastrado.")
    else:
        return produto


def completar_zeros(numero):
    total_de_digitos = 4
    zeros_restantes = total_de_digitos - len(str(numero))
    string_numerica = ""
    for casa in range(zeros_restantes):
        string_numerica = string_numerica + "0"
    string_numerica = string_numerica + str(numero)
    return string_numerica


# FLUXO PRINCIPAL DA APLICAÇÃO
opcao_escolhida = ""
while True:
    exibir_menu_inicial()
    opcao_escolhida = input("Opção escolhida -> ")
    if opcao_escolhida == "1":
        exibir_estoque()
    elif opcao_escolhida == "2":
        exibir_vendas()
    elif opcao_escolhida == "3":
        exibir_compras()
    elif opcao_escolhida == "4":
        cadastar_produto()
    elif opcao_escolhida == "5":
        cadastrar_venda()
    elif opcao_escolhida == "6":
        cadastrar_compra()
    elif opcao_escolhida == "7":
        print("Encerrando aplicação...")
        break
    else:
        print(
            f"[{opcao_escolhida}] não é uma opção válida. Por favor, tente novamente."
        )

# FIM DA APLICAÇÃO