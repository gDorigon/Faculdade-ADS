import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "categoria": [
        "Eletrônicos",
        "Roupas",
        "Alimentos",
        "Livros",
        "Móveis"
    ],
    "quantidade_vendida": [35, 50, 80, 25, 15]
}

vendas = pd.DataFrame(dados)

plt.bar(
    vendas["categoria"],
    vendas["quantidade_vendida"],
    color="royalblue"
)

plt.title("Produtos vendidos por categoria")
plt.xlabel("Categoria")
plt.ylabel("Quantidade vendida")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()