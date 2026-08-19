// Ler os valores de quatro notas escolares bimestrais de um aluno. Calcular a média aritmética desse aluno e
// apresentar a mensagem "Aprovado" se a média obtida for maior ou igual a 7; caso contrário, o programa deve
// solicitar a quinta nota (nota de exame) do aluno e calcular uma nova média aritmética entre a nota de exame e
// a primeira média aritmética. Se o valor da nova média for maior ou igual a sete, apresentar a mensagem
// "Aprovado em exame"; caso contrário, apresentar a mensagem "Reprovado". Informar também, após a
// apresentação das mensagens, o valor da média obtida pelo aluno

#include <stdio.h>
#include <stdlib.h>

int main() {
    float nota1, nota2, nota3, nota4, media, notaExame, novaMedia;

    printf("Insira a primeira nota: ");
    scanf("%f", &nota1);
    printf("Insira a segunda nota: ");
    scanf("%f", &nota2);
    printf("Insira a terceira nota: ");
    scanf("%f", &nota3);
    printf("Insira a quarta nota: ");
    scanf("%f", &nota4);

    media = (nota1 + nota2 + nota3 + nota4) / 4;

    if (media >= 7) {
        printf("Aprovado\n");
        printf("Média: %.2f\n", media);
    } else {
        printf("Reprovado. Insira a nota de exame: ");
        scanf("%f", &notaExame);
        novaMedia = (media + notaExame) / 2;

        if (novaMedia >= 7) {
            printf("Aprovado em exame\n");
        } else {
            printf("Reprovado\n");
        }
        printf("Nova média: %.2f\n", novaMedia);
    }

    return 0;
}