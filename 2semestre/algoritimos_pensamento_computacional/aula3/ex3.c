// Efetuar a leitura de três valores numéricos e processar o cálculo da equação completa de segundo grau,
// utilizando a fórmula de Bhaskara (considerar para a solução do problema todas as possíveis condições para
// delta: delta < 0 - não há solução real, delta > 0 - há duas soluções reais e diferentes e delta = 0 - há apenas
// uma solução real). Lembre-se de que é completa a equação de segundo grau que possui todos os coeficientes
// A, B e C diferentes de zero. O programa deve apresentar respostas para todas as condições estabelecidas para
// delta.

#include <stdio.h>
#include <math.h>

int main() {
    float a, b, c, delta, x1, x2;

    printf("Insira o valor de A (diferente de zero): ");
    scanf("%f", &a);
    if (a == 0) {
        printf("O coeficiente A deve ser diferente de zero.\n");
        return 1;
    }

    printf("Insira o valor de B: ");
    scanf("%f", &b);
    printf("Insira o valor de C: ");
    scanf("%f", &c);

    delta = b * b - 4 * a * c;

    if (delta < 0) {
        printf("Não há solução real.\n");
    } else if (delta == 0) {
        x1 = -b / (2 * a);
        printf("Há apenas uma solução real: x = %.2f\n", x1);
    } else {
        x1 = (-b + sqrt(delta)) / (2 * a);
        x2 = (-b - sqrt(delta)) / (2 * a);
        printf("Há duas soluções reais diferentes: x1 = %.2f e x2 = %.2f\n", x1, x2);
    }

    return 0;
}