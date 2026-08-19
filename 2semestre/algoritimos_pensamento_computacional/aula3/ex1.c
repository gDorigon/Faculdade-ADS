#include <stdlib.h>
#include <stdio.h>

int main() {
    int num1, num2, diferenca;
    printf("Insira o primeiro número: ");
    scanf("%d", &num1);
    printf("Insira o segundo número: ");
    scanf("%d", &num2);
    if(num1 > num2) {
        diferenca = num1 - num2;
    } else {
        diferenca = num2 - num1;
    }
    printf("A diferença entre os números é: %d\n", diferenca);
}