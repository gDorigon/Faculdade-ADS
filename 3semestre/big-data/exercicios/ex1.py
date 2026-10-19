import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "João", "Mariana", "Pedro"],
    "idade": [25, 32, 28, 40, 35],
    "cidade": ["São Paulo", "Curitiba", "Recife", "Salvador", "Campinas"],
    "produto_comprado": ["Notebook", "Celular", "Mouse", "Tablet", "Teclado"]
}

clientes = pd.DataFrame(dados)

print(clientes.head())