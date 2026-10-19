import pandas as pd

dados = {
    "nome": ["Ana", "Carlos", "João", "Mariana", "Pedro"],
    "idade": [25, 32, 28, 40, 35],
    "cidade": ["São Paulo", "Curitiba", "Recife", "Salvador", "Campinas"],
    "produto_comprado": [
        "Notebook",
        "Celular",
        "Mouse",
        "Tablet",
        "Teclado"
    ]
}

clientes = pd.DataFrame(dados)

idade_media = clientes["idade"].mean()
idade_maxima = clientes["idade"].max()
idade_minima = clientes["idade"].min()

print("Idade média:", idade_media)
print("Idade máxima:", idade_maxima)
print("Idade mínima:", idade_minima)