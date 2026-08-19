//Ler três valores inteiros e apresentar os valores lidos dispostos em ordem crescente.

#include <stdlib.h>
#include <stdio.h>

int main() {
    printf("Informe um numero inteiro: ");
    int num;
    scanf("%d", &num);
    printf("Informe um numero inteiro: ");
    int num2;
    scanf("%d", &num2);
    printf("Informe um numero inteiro: ");
    int num3;
    scanf("%d", &num3);

    if(num < num2 && num < num3) {
        if(num2 < num3) {
            printf("Ordem crescente: %d, %d, %d\n", num, num2, num3);
        } else {
            printf("Ordem crescente: %d, %d, %d\n", num, num3, num2);
        }
    } else if(num2 < num && num2 < num3) {
        if(num < num3) {
            printf("Ordem crescente: %d, %d, %d\n", num2, num, num3);
        } else {
            printf("Ordem crescente: %d, %d, %d\n", num2, num3, num);
        }
    } else {
        if(num < num2) {
            printf("Ordem crescente: %d, %d, %d\n", num3, num, num2);
        } else {
            printf("Ordem crescente: %d, %d, %d\n", num3, num2, num);
        }
    }


}