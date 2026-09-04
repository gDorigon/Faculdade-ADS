// d) Escrever um programa que apresente como resultado a potência de uma base qualquer elevada a um expoente qualquer, ou seja, de BS^EX, em que BS é o valor da base e EX o valor do expoente. Considere apenas a entrada de valores inteiros e positivos, ou seja, de valores naturais. Use a técnica de laço de repetição, em que o valor da base deve ser multiplicado o número de vezes determinado no expoente.

#include <stdio.h>

int main()
{
    int base, expoente, resultado = 1, i;

    printf("Digite a base (número inteiro positivo): ");
    scanf("%d", &base);

    printf("Digite o expoente (número inteiro positivo): ");
    scanf("%d", &expoente);

    for (i = 1; i <= expoente; i++)
    {
        resultado *= base;
    }

    printf("%d elevado a %d é: %d\n", base, expoente, resultado);
    return 0;
}