# Alunos:
# Nome: ______________________________  RA: _________
# Nome: ______________________________  RA: _________
# Nome: ______________________________  RA: _________
#
# Projeto Final - Entrega 4
# Modulo de Faturamento e Assinaturas de Clientes
# Professor: Me. Joao Victor Ramos

# Banco de dados em memoria (dicionario principal)
# Chave: ID do cliente | Valor: dados da assinatura
banco = {}


# Registra o log de auditoria a cada operacao
def registrar_log(operacao):
    print(f"  [LOG] {operacao}")


# Valida o ID: nao pode ser zero ou negativo
def validar_id(id_cliente):
    if id_cliente <= 0:
        raise ValueError("ID deve ser maior que zero!")


# Valida a vigencia: deve ser entre 1 e 60 meses
def validar_meses(meses):
    if meses < 1 or meses > 60:
        raise ValueError("Vigencia deve ser entre 1 e 60 meses!")


# Valida o valor do plano: nao pode ser zero ou negativo
def validar_valor(valor):
    if valor <= 0:
        raise ValueError("Valor do plano deve ser maior que zero!")


# Cadastra um novo cliente no banco
def cadastrar(banco, id_cliente, nome, plano, meses, valor):
    try:
        validar_id(id_cliente)
        validar_meses(meses)
        validar_valor(valor)
        if id_cliente in banco:
            raise KeyError("Ja existe cliente com esse ID!")
    except ValueError as e:
        print(f"  Erro: {e}")
    except KeyError as e:
        print(f"  Erro: {e}")
    else:
        # So cadastra se nao houve nenhum erro
        banco[id_cliente] = {
            "nome": nome,
            "plano": plano,
            "meses": meses,
            "valor": valor,
            "total": round(meses * valor, 2)
        }
        print(f"  Cliente #{id_cliente} cadastrado com sucesso!")
    finally:
        registrar_log("Cadastro")


# Pesquisa e exibe os dados de um cliente
def pesquisar(banco, id_cliente):
    try:
        validar_id(id_cliente)
        dados = banco[id_cliente]
    except ValueError as e:
        print(f"  Erro: {e}")
    except KeyError:
        print(f"  Erro: Cliente #{id_cliente} nao encontrado!")
    else:
        # So exibe se encontrou o cliente
        print(f"\n  --- Cliente #{id_cliente} ---")
        print(f"  Nome   : {dados['nome']}")
        print(f"  Plano  : {dados['plano']}")
        print(f"  Meses  : {dados['meses']}")
        print(f"  Valor  : R$ {dados['valor']:.2f}/mes")
        print(f"  Total  : R$ {dados['total']:.2f}")
    finally:
        registrar_log("Pesquisa")


# Lista todos os clientes cadastrados
def listar(banco):
    try:
        if not banco:
            raise ValueError("Nenhum cliente cadastrado!")
    except ValueError as e:
        print(f"  Aviso: {e}")
    else:
        # So lista se houver clientes
        print("\n  --- Lista de Clientes ---")
        for id_c, d in banco.items():
            print(f"  ID: {id_c} | Nome: {d['nome']} | Plano: {d['plano']} | {d['meses']} meses | R$ {d['valor']:.2f}/mes | Total: R$ {d['total']:.2f}")
    finally:
        registrar_log("Listagem")


# Atualiza a assinatura de um cliente existente
def atualizar(banco, id_cliente, plano, meses, valor):
    try:
        validar_id(id_cliente)
        validar_meses(meses)
        validar_valor(valor)
        if id_cliente not in banco:
            raise KeyError(f"Cliente #{id_cliente} nao existe!")
    except ValueError as e:
        print(f"  Erro: {e}")
    except KeyError as e:
        print(f"  Erro: {e}")
    else:
        # So atualiza se passou por todas as validacoes
        banco[id_cliente]["plano"] = plano
        banco[id_cliente]["meses"] = meses
        banco[id_cliente]["valor"] = valor
        banco[id_cliente]["total"] = round(meses * valor, 2)
        print(f"  Assinatura do cliente #{id_cliente} atualizada!")
    finally:
        registrar_log("Atualizacao")


# Funcao principal com o menu
def main():
    print("=== SISTEMA DE ASSINATURAS ===")

    while True:
        print("\n1. Cadastrar cliente")
        print("2. Pesquisar cliente")
        print("3. Listar clientes")
        print("4. Atualizar assinatura")
        print("0. Sair")

        try:
            opcao = int(input("Opcao: "))
        except ValueError:
            print("  Digite apenas numeros!")
            continue

        if opcao == 1:
            # Coleta os dados do novo cliente
            while True:
                try:
                    id_c = int(input("ID do cliente: "))
                    break
                except ValueError:
                    print("  Digite apenas numeros!")

            nome = input("Nome: ").strip()
            while not nome:
                print("  Nome nao pode ser vazio!")
                nome = input("Nome: ").strip()

            plano = input("Plano (ex: BASICO, PREMIUM): ").strip().upper()

            while True:
                try:
                    meses = int(input("Vigencia (meses): "))
                    break
                except ValueError:
                    print("  Digite apenas numeros!")

            while True:
                try:
                    valor = float(input("Valor mensal R$: "))
                    break
                except ValueError:
                    print("  Digite apenas numeros!")

            cadastrar(banco, id_c, nome, plano, meses, valor)

        elif opcao == 2:
            while True:
                try:
                    id_c = int(input("ID do cliente: "))
                    break
                except ValueError:
                    print("  Digite apenas numeros!")

            pesquisar(banco, id_c)

        elif opcao == 3:
            listar(banco)

        elif opcao == 4:
            while True:
                try:
                    id_c = int(input("ID do cliente: "))
                    break
                except ValueError:
                    print("  Digite apenas numeros!")

            plano = input("Novo plano: ").strip().upper()

            while True:
                try:
                    meses = int(input("Nova vigencia (meses): "))
                    break
                except ValueError:
                    print("  Digite apenas numeros!")

            while True:
                try:
                    valor = float(input("Novo valor mensal R$: "))
                    break
                except ValueError:
                    print("  Digite apenas numeros!")

            atualizar(banco, id_c, plano, meses, valor)

        elif opcao == 0:
            print("Encerrando. Ate logo!")
            break

        else:
            print("  Opcao invalida!")


main()
