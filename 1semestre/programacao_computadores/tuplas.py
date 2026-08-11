# Desafio de Fixação (Mão na Massa)

# 1. Crie um script que receba o nome de 5 produtos e armazene-os em uma lista. Após a entrada, o programa deve exibir os nomes em ordem alfabética e informar qual é o produto que está na posição central da lista.

# produto =  []
# for i in range(5):
#     produto.append(input(f"Digite o nome do produto {i+1}: "))

# produto.sort()
# print("Produtos em ordem alfabética: \n", produto)
# print("Produdo do meio: ", produto[2])




# Nível: Básico (Sintaxe e Acesso)

# 2. Criação e Acesso: Crie uma lista com 5 nomes de cidades. Imprima apenas a primeira e a última cidade da lista.

# cidades = ["Londrina", "Cambé", "Rolândia", "Maringá", "Curitiba"]
# print("Primeira cidade:", cidades[0])
# print("Última cidade:", cidades[-1])




# 3. Alteração Manual: Dada a lista numeros = [10, 20, 30, 40, 50], altere o valor do terceiro elemento para 100 e imprima a lista atualizada.

# numeros = [10, 20, 30, 40, 50]
# numeros[2] = 100
# print("Lista atualizada:", numeros)




# 4. Uso da Tupla: Crie uma tupla com os meses do ano. Tente alterar o primeiro mês para "Janeiro Alterado" e observe o erro gerado pelo Python. Escreva em um comentário por que o erro ocorreu.

# meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
# meses[0] = "Janeiro Alterado"  
# O erro ocorre porque as tuplas são imutáveis




# Nível: Intermediário (Métodos e Laços)

# 5. Entrada Dinâmica: Crie um programa que peça ao usuário 5 números, adicione-os em uma lista usando .append() e, ao final, exiba a soma de todos os itens (use a função sum()).

# numeros = []
# for i in range(5):
#     num = float(input(f"Digite o número {i+1}: "))
#     numeros.append(num)

# print("Soma dos números:", sum(numeros))




# 6. Ordenação de Nomes: Peça ao usuário nomes de convidados até que ele digite "fim". Guarde os nomes em uma lista, coloque-os em ordem alfabética e exiba a lista final.

# nomes = []
# while True:
#     nome = input("Digite o nome do convidado (ou 'fim' para encerrar): ")
#     if nome.lower() == "fim":
#         break
#     nomes.append(nome)

# nomes.sort()
# print("Convidados em ordem alfabética:")
# for nome in nomes:
#     print(nome)



# 7. Fatiamento (Slicing): Crie uma lista de 1 a 10. Use o fatiamento para extrair e imprimir apenas os números do índice 2 ao 7.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Números do índice 2 ao 7:", numeros[2:8])





# 8. Busca de Item: Crie uma lista de cores. Peça ao usuário para digitar uma cor e, usando o operador in, verifique se a cor está na lista. Informe o resultado.

# cores = ["vermelho", "azul", "verde", "amarelo", "preto"]
# cor_usuario = input("Digite uma cor: ").lower()
# if cor_usuario in cores:
#     print(f"A cor {cor_usuario} está na lista.")
# else:    
#     print(f"A cor {cor_usuario} não está na lista.")






# Nível: Avançado (Lógica e Processamento)

# 9. Remoção de Duplicatas: Dada uma lista com números repetidos, crie uma nova lista que contenha apenas os números únicos da lista original (dica: percorra a lista original com um for).

# listaOriginal = [1, 2, 3, 4, 2, 5, 1, 6]
# listaUnica = []
# for numero in listaOriginal:
#     if numero not in listaUnica:
#         listaUnica.append(numero)
# print("Lista original:", listaOriginal)
# print("Lista sem duplicatas:", listaUnica)




# 10. Filtro de Dados: Peça 10 notas de alunos e armazene em uma lista. Calcule a média e, em seguida, exiba apenas as notas que ficaram abaixo da média da turma.

# notas = []
# for i in range(10):
#     nota = float(input(f"Digite a nota do aluno {i+1}: "))
#     notas.append(nota)
# media = sum(notas) / len(notas)
# print("Média da turma:", media)
# print("Notas abaixo da média:")
# for nota in notas:
#     if nota < media:
#         print(nota)




# 11. Matriz Simples (Desafio): Crie uma lista chamada estoque que contenha 3 sublistas. Cada sublista deve ter [nome_produto, quantidade]. Percorra essa lista e imprima o nome de cada produto e o total de itens no estoque somando todas as quantidades.

# estoque = [
#     ["Arroz", 10],
#     ["Feijão", 5],
#     ["Macarrão", 8]
# ]

# total_itens = 0
# for produto in estoque:
#     nome_produto = produto[0]
#     quantidade = produto[1]
#     total_itens += quantidade
#     print(f"Produto: {nome_produto}, Quantidade: {quantidade}")
# print("Total de itens no estoque:", total_itens)    
