numeroTabuada = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {numeroTabuada}:")
for i in range(1, 11):
    print(f"{numeroTabuada} x {i} = {numeroTabuada * i}")