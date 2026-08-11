    # Nomes: [ADICIONE AQUI OS NOMES E RAs DOS INTEGRANTES]
    # Programa de Controle de Fluxo e Coleções
    # Professor: Me João Víctor Ramos
    # Data: 12/05/2026

    # --- INÍCIO DO PROGRAMA ---

    import random

    # Dicionário de estoque (produto: quantidade)
    estoque = {}

    # Lista para registrar o histórico das movimentações
    historico = []

    def mostrar_estoque():
        print("\n--- ESTOQUE ATUAL ---")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade}")

    def retirar_produto():
        print("\n--- RETIRADA DE PRODUTO ---")
        produto = input("Digite o nome do produto: ").strip().title()
        if produto not in estoque:
            print("Produto não encontrado no estoque.")
            return
        try:
            qtd = int(input(f"Quantidade de {produto} para retirar: "))
            if qtd <= 0:
                print("Quantidade deve ser positiva.")
                return
        except ValueError:
            print("Digite um número válido para a quantidade.")
            return
        if estoque[produto] < qtd:
            print(f"Não há quantidade suficiente de {produto} no estoque.")
            return
        estoque[produto] -= qtd
        msg = f"Retirada de {qtd} {produto}{'s' if qtd > 1 else ''}"
        historico.append(msg)
        print(f"{msg} realizada com sucesso!")

    def mostrar_historico():
        print("\n--- HISTÓRICO DE MOVIMENTAÇÕES ---")
        if not historico:
            print("Nenhuma movimentação registrada.")
        else:
            for item in historico:
                print(item)

    def sorteio_final():
        print("\n--- SORTEIO FINAL ---")
        if not historico:
            print("Nenhuma movimentação registrada. Não é possível sortear.")
            return
        sorteado = random.choice(historico)
        print(f"O sorteado da rodada, baseado na movimentação '{sorteado}', ganhou um brinde!")

    # Laço principal do menu
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1. Consultar Estoque")
        print("2. Retirar Produto")
        print("3. Ver Histórico")
        print("4. Sair e Sortear Brinde")
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == '1':
            mostrar_estoque()
        elif opcao == '2':
            retirar_produto()
        elif opcao == '3':
            mostrar_historico()
        elif opcao == '4':
            sorteio_final()
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

    # --- FIM DO PROGRAMA ---
    estoque = {}

    while True:
        print(" --- Estoque ---")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Exibir estoque")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")
        case escolha:        
            case "1":
                nome = input("Digite o nome do produto: ")
                quantidade = int(input("Digite a quantidade: "))
                if nome in estoque:
                    estoque[nome] += quantidade
                else:                estoque[nome] = quantidade
                print(f"{quantidade} unidades de {nome} adicionadas ao estoque.")
            case "2":
                nome = input("Digite o nome do produto: ")
                quantidade = int(input("Digite a quantidade: "))
                if nome in estoque:
                    if estoque[nome] >= quantidade:
                        estoque[nome] -= quantidade
                        print(f"{quantidade} unidades de {nome} removidas do estoque.")
                    else:
                        print(f"Quantidade insuficiente de {nome} em estoque.")
                else:
                    print(f"{nome} não encontrado em estoque.")
            case "3":
                if estoque:
                    print("Estoque atual:")
                    for produto, quantidade in estoque.items():
                        print(f"{produto}: {quantidade} unidades")
                else:                    print("O estoque está vazio.")
            case "4":
                print("Saindo do programa. Obrigado!")
                break
            case _:             print("Opção inválida. Por favor, tente novamente.")    