# Alunos:
# Guilherme Dorigon
# João Victor
# Vinicius
# Renan
# Henrique

nomeGestor = input("Digite o nome do gestor. \nR: ")
mesReferencia = input("Digite o mês de referência. \nR: ")
periodo = input(f"Informe quantos dias do mês: {mesReferencia} vão ser registrados.\nR: ")

# Inicialização das variaveis
total = 0
menorVenda = 0
maiorVenda = 0
mediaDeVendas = 0
diasSemVendas = 0
eficiencia = 0

# Looping para perguntar o valor de venda de cada dia do periodo informado
for i in range(int(periodo)):
    valorDia = float(input(f"\nDigite o valor de vendas no dia {i+1}: \nR: "))
    total += valorDia # Adiciona o valor do dia no total

    if valorDia < menorVenda or menorVenda == 0: # Salva o valor do dia com menor valor de venda, e compara todo novo valor para ver se é menor que o menor registro salvo
        menorVenda = valorDia
    if valorDia > maiorVenda: # Salva o maior valor de venda e também compara com todo novo valor, caso o valor inserido deja maior que o registro salvo, atualiza o valor registrado
        maiorVenda = valorDia
    if valorDia == 0: # contador de dias sem vendas
        diasSemVendas += 1

eficiencia = (total / 10000) * 100 # Calculo de porcentagem em cima da meta de vendas e do total
print("\n\n\n------< Relatório de Vendas >------")
print(f"Gestor: {nomeGestor}")
print(f"Mês de referência: {mesReferencia}")
print(f"Vigência: {periodo} dias")
print("-----------------------------------")
print(f"total vendas: {total:.2f}")
if total > 10000:
    print("Meta de vendas atingida.")
else:
    print(f"Meta de vendas não atingida, faltou: {10000 - total}")
if diasSemVendas > 0:
    print(f"Dias sem vendas: {diasSemVendas}")
else:
    print("Nenhum dia sem vendas.")
print("-----------------------------------")
print(f"média de vendas (por dia): {total / int(periodo):.2f}") # calculo da média de vendas por dia, total dividido pela quantidade de dias do periodo
print(f"menor venda: {menorVenda}")
print(f"maior venda: {maiorVenda}")
print("-----------------------------------")
print(f"eficiência: {eficiencia:.2f}%")
if eficiencia < 85:
    print("Aproveitamento Regular")
elif eficiencia >= 85 and eficiencia <= 100:
    print("Aproveitamento Bom")
elif eficiencia > 100 and eficiencia < 125:
    print("Aproveitamento Ótimo")
elif eficiencia >= 125:
    print("Aproveitamento Excelente")
print("------< Fim do relatório >------")