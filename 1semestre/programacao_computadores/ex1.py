# Guilherme Dorigon Bovo

# Exercicio 1
# Peça a idade do usuário e diga se ele é maior ou menor de idade

# idade = int(input("Informe a sua idade: "))
# if idade <= 18:
#     print("Você é menor de idade.")
# elif idade < 18:
#     print("Você é menor de idade")

# Exercicio 2
# Receba um número e informe se ele é positivo, negativo ou zero.

# numero = float(input("Informe um número: "))
# if numero > 0:
#     print("O número é positivo.")
# elif numero < 0:
#     print("O número é negativo.")
# else:
#     print("O número é zero.")

# Exercicio 3
# Receba um núnero interio e diga se ele é par ou ímpar.

# numero = int(input("Informe um número inteiro: "))
# if numero % 2 == 0:
#     print("O número é par.")
# else:
#     print("O número é ímpar.")

# Exercicio 4
# Peça duas notas, calcuke a média e diga aprovado se a média for 7.0 ou superior, caso contrario diga reprovado.
# nota1 = float(input("Informe a primeira nota: "))
# nota2 = float(input("Informe a segunda nota: "))
# media = (nota1 + nota2) / 2
# if media >= 7.0:
#     print("Aprovado, com média: {:.2f}".format(media))
# else:
#     print("Reprovado, com média: {:.2f}".format(media))

#Exercicio 5
# peça 2 numeros e diga qual é o maior

# num1 = float(input("Informe o primeiro número: "))
# num2 = float(input("Informe o segundo número: "))
# if num1 > num2:
#     print("O primeiro número é maior.")
# elif num2 > num1:
#     print("O segundo número é maior.")
# else:
#     print("Os números são iguais.")

# Exercicio 6
#Receba a idade de um nadador e classifique 5-7 ( Infantil A), 8-10 (Infantil B), 11-13 (Juvenil A), 14-17 (Juvenil B) e 18+ (Adulto)

# idade = int(input("Informe a idade do nadador: "))
# if 5 <= idade <= 7:
#     print("Classificação: Infantil A")
# elif 8 <= idade <= 10:
#     print("Classificação: Infantil B")
# elif 11 <= idade <= 13:
#     print("Classificação: Juvenil A")
# elif 14 <= idade <= 17:
#     print("Classificação: Juvenil B")
# else idade >= 18:
#     print("Classificação: Adulto")

#Exercicio 7
# Calculadora de IMC
# peso = float(input("Informe o peso em kg: "))
# altura = float(input("Informe a altura em metros: "))
# imc = peso / (altura ** 2)
# print(f"O IMC é: {imc:.2f}")
# if imc < 18.5:
#     print("Classificação: Abaixo do peso")
# elif 18.5 <= imc < 25:
#     print("Classificação: Peso normal")
# elif imc >= 25:
#     print("Classificação: Acima do peso")

# Exercicio 8
# peça a temperatura e peca se o usuario quer converter para Celsius ou Fahrenheit
# temperatura = float(input("Informe a temperatura: "))
# unidade = input("Deseja converter para Celsius (C) ou Fahrenheit (F)? ").upper()
# if unidade == "C":
#     temperatura_convertida = (temperatura - 32) * 5 / 9
#     print(f"A temperatura convertida para Celsius é: {temperatura_convertida:.2f} °C")
# elif unidade == "F":
#     temperatura_convertida = (temperatura * 9 / 5) + 32
#     print(f"A temperatura convertida para Fahrenheit é: {temperatura_convertida:.2f} °F")
# else:
#     print("Unidade de conversão inválida. Por favor, escolha 'C' para Celsius ou 'F' para Fahrenheit.")

# Exercicio 9
# Categorize um produto, caso menor que 50, barato, entre 50 e 100, normal, acima de 100, caro

# preco = float(input("Informe o preço do produto: "))
# if preco < 50:
#     print("barato")
# elif 50 <= preco <= 100:
#     print("médio")
# else:    
#     print("caro")

# Exercicio 10
# Pergunte o turno de estudo do aluno (M - matutino, V - vespertino, N - noturno) e imprima uma mensagem de acordo com a escolha.

# turno = input("Informe o turno de estudo do aluno (M - matutino, V - vespertino, N - noturno): ").upper()
# if turno == "M":
#     print("Bom dia")
# elif turno == "V":
#     print("Boa tarde")
# elif turno == "N":
#     print("Boa noite")

# Exercicio 11
# sistema simples de acesso
# acesso = ["admin", "fatec123"]

# usuario = input("Informe o nome de usuário: ")
# senha = input("Informe a senha: ")

# if usuario == acesso[0] and senha == acesso[1]:
#     print("Acesso concedido.")
# else:
#     print("Acesso negado. Usuário ou senha incorretos.")

# Exercicio 12
# Receba três lados (A, B, C). Verifique se podem formar um triângulo: (A < B+C) e (B < A+C) e (C < A+B)

# ladoA = float(input("Informe o valor do lado A: "))
# ladoB = float(input("Informe o valor do lado B: "))
# ladoC = float(input("Informe o valor do lado C: "))
# if (ladoA < ladoB + ladoC) and (ladoB < ladoA + ladoC) and (ladoC < ladoA + ladoB):
#     print("Os lados podem formar um triângulo.")
# else:    
#     print("Os lados não podem formar um triângulo.")

# Exercicio 13
# Peça a idade do usuário e diga se o voto dele é obrigatório ou facultativo.

# idade = int(input("Informe a sua idade: "))
# if idade < 16:
#     print("Voto não permitido.")
# elif 16 <= idade < 18 or idade >= 70:
#     print("Voto facultativo.")
# else:
#     print("Voto obrigatório.")

# Exercicio 14
# Desconto no valor do pedido se a pessoa for maior de 65 anos e a compra for acima de 100 reais

# idade = int(input("Informe a idade do cliente: "))
# valor_compra = float(input("Informe o valor da compra: "))
# if idade > 65 and valor_compra > 100:
#     print("Desconto aplicado.")
# else:
#     print("Desconto não aplicado.")

# Exercicio 15
#Um ano é bissexto se for divisível por 4 e (não divisível por 100 ou divisível por 400). Peça um ano e verifique.

# ano = int(input("Informe um ano: "))
# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print(f"O ano {ano} é bissexto.")
# else:    
#     print(f"O ano {ano} não é bissexto.")

# Exercicio 16
#Sistema de Empréstimo: Pergunte o valor do empréstimo e a renda mensal. Se a renda for maior que R$ 2000, pergunte em quantas parcelas. Se a parcela exceder 30% da renda, negue o empréstimo; caso contrário, aprove.

# valor_emprestimo = float(input("Informe o valor do empréstimo: "))
# renda_mensal = float(input("Informe a renda mensal: "))
# if renda_mensal > 2000:
#     parcelas = int(input("Informe o número de parcelas: "))
#     valor_parcela = valor_emprestimo / parcelas
#     if valor_parcela > 0.3 * renda_mensal:
#         print("Empréstimo negado. A parcela excede 30% da renda.")
#     else:
#         print("Empréstimo aprovado.")
# else:
#     print("Empréstimo negado. Renda mensal insuficiente.")


# Exercicio 17
#Login com Níveis: Peça o login. Se for "admin", peça a senha. Se a senha estiver correta, pergunte se quer "Reiniciar Sistema" ou "Desligar". Se o login não for "admin", diga "Acesso de Usuário Comum".

# login = input("Informe o login: ")
# if login == "admin":
#     senha = input("Informe a senha: ")
#     if senha == "admin123":
#         acao = input("Deseja 'Reiniciar Sistema' ou 'Desligar'? ").lower()
#         if acao == "reiniciar sistema":
#             print("Sistema reiniciado.")
#         elif acao == "desligar":
#             print("Sistema desligado.")
#         else:
#             print("Ação inválida.")
#     else:
#         print("Senha incorreta.")
# else:
#     print("Acesso de Usuário Comum.")

# Exercicio 18
# Clima e Vestimenta: Pergunte se está chovendo (S/N). Se sim, pergunte se está ventando forte (S/N). Se chover e ventar, diga "Use capa de chuva reforçada". Se apenas chover, "Use guarda-chuva". Se não chover, diga "Tenha um bom dia".

# chovendo = input("Está chovendo? (S/N): ").upper()
# if chovendo == "S":
#     ventando = input("Está ventando forte? (S/N): ").upper()
#     if ventando == "S":
#         print("Use capa de chuva reforçada.")
#     else:
#         print("Use guarda-chuva.")
# else:
#     print("Tenha um bom dia.")

# Exercicio 19
# Raízes de Equação de 2º Grau: Peça os coeficientes A, B e C. Calcule o Delta. Se Delta < 0, diga "Não há raízes reais". Se Delta == 0, calcule e mostre a única raiz. Se Delta > 0, mostre as duas raízes. (Use math.sqrt)

# import math
# coeff_a = float(input("Informe o coeficiente A: "))
# coeff_b = float(input("Informe o coeficiente B: "))
# coeff_c = float(input("Informe o coeficiente C: "))
# delta = coeff_b**2 - 4*coeff_a*coeff_c
# if delta < 0:
#     print("Não há raízes reais.")
# elif delta == 0:
#     raiz = -coeff_b / (2 * coeff_a)
#     print(f"A única raiz é: {raiz:.2f}")
# else:
#     raiz1 = (-coeff_b + math.sqrt(delta)) / (2 * coeff_a)
#     raiz2 = (-coeff_b - math.sqrt(delta)) / (2 * coeff_a)
#     print(f"As raízes são: {raiz1:.2f} e {raiz2:.2f}")


# Exercicio 20
# Simulador de Caixa Eletrônico: Peça o valor a ser sacado (inteiro). Verifique se o valor é múltiplo de 10 (únicas notas disponíveis). Se for, pergunte se o cliente aceita pagar uma taxa de R$ 2,00 caso o valor seja superior a R$ 500. Exiba o status final da operação.

# valor_saque = int(input("Informe o valor a ser sacado (múltiplo de 10): "))
# if valor_saque % 10 == 0:
#     if valor_saque > 500:
#         aceitar_taxa = input("O valor é superior a R$ 500. Você aceita pagar uma taxa de R$ 2,00? (S/N): ").upper()
#         if aceitar_taxa == "S":
#             valor_final = valor_saque + 2
#             print(f"Saque aprovado. Valor final com taxa: R$ {valor_final:.2f}")
#         else:
#             print("Saque negado. Taxa não aceita.")
#     else:
#         print("Saque aprovado. Valor: R$ {:.2f}".format(valor_saque))
# else:
#     print("Valor inválido. O valor deve ser múltiplo de 10.")



print("\n Fim da lista de exercicios")


def verifica_numero(nuemro_sorteado, numero_escolhido)
    if numero_escolhido > nuemro_sorteado
        print("numero esolhido é menor que o sorteado")
    elif numero_escolhido < nuemro_sorteado
        print("numero esolhido é maior que o sorteado")
    else:
        print("nuemro")
        break

    