#include <stdio.h>
#include <stdlib.h>

int main() {
    float valor;
    printf("Informe o valor em dolar: ");
    scanf("%f", &valor);

    printf("%.2fU$ em reais são: %.2fR$", valor, valor*5.18);

    return 0;
}