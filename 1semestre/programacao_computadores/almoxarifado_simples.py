"""
# Alunos
# Guilherme Dorigon - 47583029
# João Victor Linares de Jesus - 46957405
# Miguel Augusto Rivera Mendes - 48741337
# Renan Alves - 47668865
# Vinicius Azara - 47607602

# Programa de Controle de Fluxo e Coleções - ENTREGA 2
"""

import random


def registrar_log(operacao, detalhe):
    print(f"[{operacao}] {detalhe}")


def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def ler_texto_nao_vazio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Entrada vazia. Tente novamente.")


def adicionar_produto(estoque, nome, quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero")
    estoque[nome] = estoque.get(nome, 0) + quantidade
    registrar_log("ADICIONAR", f"{quantidade}x '{nome}'")


def consultar_estoque(estoque):
    if not estoque:
        print("Estoque vazio")
        return
    for item, qtd in estoque.items():
        print(f"{item}: {qtd}")


def retirar_item(estoque, historico, nome, quantidade):
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero")
    if nome not in estoque:
        raise KeyError("Produto não encontrado")
    if quantidade > estoque[nome]:
        raise ValueError("Quantidade solicitada maior que o estoque")
    estoque[nome] -= quantidade
    historico.append(f"{quantidade}x '{nome}' retirado")
    registrar_log("RETIRAR", f"{quantidade}x '{nome}'")


def ver_historico(historico):
    if not historico:
        print("Nenhuma retirada registrada.")
        return
    print("--- Histórico ---")
    for reg in historico:
        print(reg)


def finalizar_e_sortear(historico):
    if not historico:
        print("Histórico vazio. Nada para sortear.")
        return
    vencedor = random.choice(historico)
    print(f"O ganhador foi: {vencedor}")


def main():
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

    while True:
        print("--------------------------------------")
        print("Bem vindo ao sistema do almoxarifado.")
        print("0. Adicionar Produto")
        print("1. Consultar Estoque")
        print("2. Retirar Item")
        print("3. Ver Histórico")
        print("4. Sair e Sortear")
        print("--------------------------------------")
        opc = input('Escolha uma opção: ').strip()

        try:
            if opc == "0":
                nome = ler_texto_nao_vazio("Digite o nome do produto: ")
                qtd = ler_inteiro("Digite a quantidade do produto: ")
                adicionar_produto(estoque, nome, qtd)
                print(f"{qtd}x do produto '{nome}' adicionados")

            elif opc == "1":
                consultar_estoque(estoque)

            elif opc == "2":
                nome = ler_texto_nao_vazio("Digite o nome do produto: ")
                qtd = ler_inteiro("Digite a quantidade do produto: ")
                retirar_item(estoque, historico, nome, qtd)
                print(f"{qtd}x do produto '{nome}' retirados")

            elif opc == "3":
                ver_historico(historico)

            elif opc == "4":
                finalizar_e_sortear(historico)
                print("Saindo...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError as ve:
            print(f"Erro: {ve}")
        except KeyError as ke:
            print(f"Erro: {ke}")
        except KeyboardInterrupt:
            print("\nInterrompido pelo usuário. Saindo.")
            break


if __name__ == "__main__":
    main()
