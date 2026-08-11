
def calcular_divisao(valor_total, qtd_pesosas):
    if valor_total <= 0 or qtd_pessoas <= 0:
        return 'Valor total e quantidade de pessoas devem ser maiores que zero.'
        
    resultado = valor_total / qtd_pessoas
    return resultado

print("sistema de divisão de conta")

try:
    total_conta = float(input("Digite o valor total da conta: "))
    pessoas = int(input("Digite a quantidade de pessoas: "))
    valor_por_pessoa = calcular_divisao(total_conta, pessoas)

except ValueError as error:
    print("Erro de entrada: ", error)

except ZeroDivisionError as error:
    print("Erro de divisão por zero: ", error)

else:
    print(f"O valor a ser pago por cada pessoa é: R$ {valor_por_pessoa:.2f}")

finally:
    print("Obrigado por usar o sistema de divisão de conta.")

