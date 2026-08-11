

# 6.
 
# Distribuição de Doces:
 
# Uma professora tem X balas para dividir

# igualmente entre Y alunos. Quantas balas inteiras cada aluno recebe e

# quantas sobram com a professora? (Use // e %).

# 79

# 80
# 27/03/2026

# 41

# EXERCICIOS DE FIXAÇÃO

# •
 
# Nível 3: Avançado (Biblioteca
 
# math
 
# e Fórmulas)

# •
 
# Foco: Importação de módulos e funções especializadas.

# 7.
 
# Cálculo de Potência:
 
# Peça uma base e um expoente ao usuário e calcule o

# resultado usando
 
# math.pow
# ().

# 8.
 
# Raiz Quadrada de Pitágoras:
 
# Peça os valores dos dois catetos de um triângulo

# retângulo. Calcule a hipotenusa usando
 
# math.sqrt
# ().

# 9.
 
# Área e Perímetro:
 
# Peça o raio de um círculo. Exiba a área e o perímetro

# utilizando a constante
 
# math.pi
# .

# 10.
 
# O Teto da Obra:
 
# Um galão de tinta pinta 15 metros quadrados. Peça ao usuário

# a área que ele deseja pintar e diga quantos galões ele precisa comprar. (Dica:

# Use
 
# math.ceil
# (), pois não se vende meio galão).

# EXERCICIOS DE FIXAÇÃO

# •
 
# Nível 4: Desafio de Pensamento Computacional

# •
 
# Foco: Decomposição de problemas.

# 11.
 
# Decomposição de Tempo:
 
# Peça ao usuário um valor em
 
# segundos
# .

# Converta e exiba quantos minutos e quantos segundos esse valor

# representa (
# Ex
# : 130 segundos = 2 minutos e 10 segundos).

# 12.
 
# Cálculo de Distância:
 
# Receba as coordenadas (x1, y1) e (x2, y2) de dois

# pontos no plano cartesiano e calcule a distância entre eles usando a

# fórmula: d = √((x2 - x1)² + (y2 - y1)²).


import math
# Exercicio 1

# numero1 = float(input("Informe o valor do primeiro numero: "))
# numero2 = float(input("Informe o valor do segundo numero: "))
# print(f"A soma dos numeros é: {numero1 + numero2:.2f}")


# Exercicio 2

# ano_atual = int(input("Informe o ano atual: "))
# ano_nascimento = int(input("Informe o ano de nascimento: "))
# idade = ano_atual - ano_nascimento
# print(f"A idade aproximada é: {idade} anos.")

# Exercicio 3

# valorReais = float(input("Informe o valor em Reais: "))
# cotacaoDolar = float(input("Informe a cotação do Dólar: "))
# valorDolar = valorReais / cotacaoDolar
# print(f"O valor convertido em Dólares é: {valorDolar:.2f})")

# Exercicio 4

# nota1 = float(input("Informe a primeira nota: "))
# nota2 = float(input("Informe a segunda nota: "))
# nota3 = float(input("Informe a terceira nota: "))
# media = (nota1 + nota2 + nota3) / 3
# print(f"A média aritmética é: {media:.2f}")

# Exercicio 5

# valorConta = float(input("Informe o valor total da conta: "))
# quantidadePessoas = int(input("Informe a quantidade de pessoas: "))
# valorPorPessoa = valorConta / quantidadePessoas
# print(f"Cada pessoa deve pagar: {valorPorPessoa:.2f}")

# Exercicio 6

# balas = int(input("Informe a quantidade de balas: "))
# alunos = int(input("Informe a quantidade de alunos: "))
# balas_por_aluno = balas // alunos
# balas_sobrando = balas % alunos
# print(f"Cada aluno recebe {balas_por_aluno} balas e sobra {balas_sobrando} balas com a professora.")

# Exercicio 7

# base = float(input("Informe a base: "))
# expoente = float(input("Informe o expoente: "))
# resultado = math.pow(base, expoente)
# print(f"O resultado de {base} elevado a {expoente} é: {resultado:.2f}")

# Exercicio 8

# cateto1 = float(input("Informe o valor do primeiro cateto: "))
# cateto2 = float(input("Informe o valor do segundo cateto: "))
# hipotenusa = math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))
# print(f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")

# Exercicio 9

# raio = float(input("Informe o raio do círculo: "))
# area = math.pi * math.pow(raio, 2)
# perimetro = 2 * math.pi * raio
# print(f"A área do círculo é: {area:.2f}")
# print(f"O perímetro do círculo é: {perimetro:.2f}")

# Exercicio 10

# area_pintar = float(input("Informe a área que deseja pintar (em metros quadrados): "))
# galões_necessarios = math.ceil(area_pintar / 15)
# print(f"Você precisa comprar {galões_necessarios} galões de tinta.")

# Exercicio 11

# segundos = int(input("Informe o valor em segundos: "))
# minutos = segundos // 60
# segundos_restantes = segundos % 60
# print(f"{segundos} segundos equivalem a {minutos} minutos e {segundos_restantes} segundos.")

# Exercicio 12

# x1 = float(input("Informe a coordenada x1: "))
# y1 = float(input("Informe a coordenada y1: "))
# x2 = float(input("Informe a coordenada x2: "))
# y2 = float(input("Informe a coordenada y2: "))
# distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
# print(f"A distância entre os pontos é: {distancia:.2f}")  

# Exercicio 1
# Peça a idade do usuário e diga se ele é maior ou menor de idade

# idade = int(input("Informe a sua idade: "))
# if idade <= 18:
#     print("Você é menor de idade.")
# elif idade < 18:
#     print("Você é menor de idade")

# Exercicio 2
# Receba um número e informe se ele é positivo, negativo ou zero.

numero = float(input("Informe um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
