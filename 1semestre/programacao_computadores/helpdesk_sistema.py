# Sistema de Controle de Estoque

banco_produtos = {}


# registra tudo que vai rolando no sistema
def registrar_log(operacao):
    print(f"LOG: {operacao}")

# funções pra validar dados de entrada

def validar_id_positivo(id_produto):
    if id_produto <= 0:
        raise ValueError("ID tem que ser maior que zero!")


def validar_preco(preco):
    if preco <= 0:
        raise ValueError("Preço tem que ser maior que zero!")


def validar_quantidade(quantidade):
    if quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa!")


# lê input do usuário com segurança

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Só números inteiros!")


def ler_texto_vazio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Não pode deixar vazio!")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Só números inteiros!")


def inserir_produto(banco, id_produto, nome, preco, quantidade):
    try:
        validar_id_positivo(id_produto)
        validar_preco(preco)
        validar_quantidade(quantidade)

        if id_produto in banco:
            raise KeyError("Produto já existe!")

    except (ValueError, KeyError) as erro:
        print(f"\nErro: {erro}")

    else:
        banco[id_produto] = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
        print(f"\nProduto #{id_produto} cadastrado com sucesso!")

    finally:
        registrar_log("Inserção")

def pesquisar_produto(banco, id_produto):
    try:
        validar_id_positivo(id_produto)
        produto = banco[id_produto]

    except ValueError as erro:
        print(f"Erro: {erro}")

    except KeyError:
        print(f"Produto #{id_produto} não encontrado!")

    else:
        print(f"\n--- PRODUTO #{id_produto} ---")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")

    finally:
        registrar_log("Pesquisa")

def listar_produtos(banco):
    try:
        if not banco:
            raise ValueError("Nenhum produto cadastrado!")

    except ValueError as erro:
        print(f"\n{erro}")

    else:
        print("\n=== PRODUTOS ===")

        for id_p, dados in banco.items():
            print(
                f"ID: {id_p} | "
                f"Nome: {dados['nome']} | "
                f"Preço: R$ {dados['preco']:.2f} | "
                f"Qtd: {dados['quantidade']}"
            )

    finally:
        registrar_log("Listagem")

def movimentar_estoque(banco, id_produto, tipo_mov, quantidade):
    try:
        validar_id_positivo(id_produto)
        validar_quantidade(quantidade)

        if tipo_mov not in ("VENDA", "ENTRADA"):
            raise ValueError("Tipo deve ser VENDA ou ENTRADA")

        produto = banco[id_produto]

        if tipo_mov == "VENDA":
            if produto["quantidade"] < quantidade:
                raise ValueError("Estoque insuficiente")
            produto["quantidade"] -= quantidade
        else:
            produto["quantidade"] += quantidade

    except (ValueError, KeyError) as erro:
        print(f"\nErro: {erro}")

    else:
        print(
            f"\nMovimentação realizada! "
            f"Novo estoque: {produto['quantidade']}"
        )

    finally:
        registrar_log("Movimentação")

# interface com o usuário (menus e telas)

def exibir_menu_principal():
    print("\n" + "=" * 50)
    print("   CONTROLE DE ESTOQUE")
    print("=" * 50)
    print("  1. Cadastrar produto")
    print("  2. Pesquisar produto")
    print("  3. Listar produtos")
    print("  4. Movimentar estoque")
    print("  0. Sair")
    print("-" * 50)


def fluxo_inserir(banco):
    print("\n--- NOVO PRODUTO ---")
    id_p = ler_inteiro("  ID: ")
    nome = ler_texto_vazio("  Nome: ")
    preco = ler_float("  Preço R$: ")
    qtd = ler_inteiro("  Quantidade: ")
    inserir_produto(banco, id_p, nome, preco, qtd)


def fluxo_pesquisar(banco):
    print("\n--- PESQUISAR ---")
    id_p = ler_inteiro("  ID: ")
    pesquisar_produto(banco, id_p)


def fluxo_movimentar(banco):
    print("\n--- MOVIMENTAR ---")
    id_p = ler_inteiro("  ID: ")
    print("  Tipo: VENDA ou ENTRADA")
    tipo = ler_texto_vazio("  ? ").upper()
    qtd = ler_inteiro("  Quantidade: ")
    movimentar_estoque(banco, id_p, tipo, qtd)


# função principal que roda o programa

def main():
    print("\n=== ESTOQUE ===\n")
    
    while True:
        exibir_menu_principal()
        
        try:
            opcao = int(input("  Opção: "))
        except ValueError:
            print("Só números!")
            continue
        
        if opcao == 1:
            fluxo_inserir(banco_produtos)
        elif opcao == 2:
            fluxo_pesquisar(banco_produtos)
        elif opcao == 3:
            listar_produtos(banco_produtos)
        elif opcao == 4:
            fluxo_movimentar(banco_produtos)
        elif opcao == 0:
            print("\n  Até logo!")
            break
        else:
            print("Opção inválida")



main()
