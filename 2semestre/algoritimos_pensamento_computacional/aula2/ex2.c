// calca um codigo que calcule a soma dos quadrads de 4 numeros escolhidos

#include <stdio.h>
int main() {
    int num1, num2, num3, num4;
    printf("Informe quatro numeros inteiros: ");
    scanf("%d %d %d %d", &num1, &num2, &num3, &num4);
    int somaQuadrados = (num1 * num1) + (num2 * num2) + (num3 * num3) + (num4 * num4);
    printf("A soma dos quadrados dos numeros informados é: %d\n", somaQuadrados);
    return 0;
}