#include <stdio.h>
#include <stdlib.h>


int main(){
    int number, rounds;

    printf("\n\n\nDigite o número que deseja saber se é primo: ");
    scanf("%d", &number);

    if(number%2==0) {
        printf("\n\nÉ composto!\n\n");
        return 0;
    }

    printf("Digite a quantidade de rounds que deseja executar: ");
    scanf("%d", &rounds);

    

}