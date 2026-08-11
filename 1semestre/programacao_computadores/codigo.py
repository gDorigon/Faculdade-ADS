banco_produtos = {}

def registra_log(operacao):
    print(f"LOG: {operacao}")
    
def validar_id_positivo(id_produto):
    if id_produto <= 0:
        raise ValueError("ID deve ser maior que zero!")

def validar_preco(preco):
    if preco <= 0:
        raise ValueError("Preço deve ser maior que zero!") 

def validar_quantidade(quantidade):
    if quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa!")

def valida_intero(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Só números inteiros!") 

def valida_texto_vazio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Não pode deixar vazio!")


def cadastra_produto(banco, id_produto, nome, preco, quantidade):
    try:
        validar_id_positivo(id_produto)
        validar_preco(preco)
        validar_quantidade(quantidade)

        if id_produto in banco:
            raise KeyError("Produto já existe!")

    except (ValueError, KeyError) as erro:
        print(f"Erro: {erro}")

    else:
        banco[id_produto] = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }
        registra_log(f"Produto #{id_produto} cadastrado")