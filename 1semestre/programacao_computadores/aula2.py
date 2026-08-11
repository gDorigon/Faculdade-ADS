import numpy as np
import matplotlib.pyplot as plt

# tamanho do mapa
largura = 200
altura = 200

# gera ruído aleatório
mapa = np.random.rand(altura, largura)

# suaviza o mapa várias vezes (simula noise tipo Perlin)
for _ in range(8):
    mapa = (
        mapa +
        np.roll(mapa, 1, axis=0) +
        np.roll(mapa, -1, axis=0) +
        np.roll(mapa, 1, axis=1) +
        np.roll(mapa, -1, axis=1)
    ) / 5

# cria mapa de terreno
terreno = np.zeros((altura, largura, 3))

for y in range(altura):
    for x in range(largura):

        v = mapa[y][x]

        if v < 0.4:          # água
            terreno[y][x] = [0, 0.2, 0.8]

        elif v < 0.5:        # praia
            terreno[y][x] = [0.9, 0.85, 0.6]

        elif v < 0.7:        # grama
            terreno[y][x] = [0.1, 0.7, 0.2]

        elif v < 0.85:       # floresta
            terreno[y][x] = [0.0, 0.4, 0.0]

        else:                # montanha
            terreno[y][x] = [0.5, 0.5, 0.5]


plt.figure(figsize=(8,8))
plt.imshow(terreno)
plt.axis("off")
plt.title("Mapa Procedural Gerado")
plt.show()