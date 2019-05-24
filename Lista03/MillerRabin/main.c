#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


int MRA(long long number,int rounds)
{
    int i;
    long long even_number;
    double d_rounds, percentage;

    if (number < 2)
    {
        printf("\n\t%lld é composto\n\n\n", number);
        return 0;
    }
    if (number != 2 && number % 2==0)
    {
        printf("\n\t%lld é composto\n\n\n", number);
        return 0;
    }
    
    even_number = number - 1;
    while (even_number % 2 == 0)
    {
        even_number /= 2;

    }

    for (i = 0; i < rounds; i++)
    {
        long long temp = even_number;
        long long randon = rand() % (number - 1) + 1;

        printf("\n\n%lld", temp);
        printf("\n\n%lld", random);

    }

}



int main(){
    long long number;
    int rounds;

    printf("\n\n\nDigite o número que deseja saber se é primo: ");
    // scanf("%lld", &number);
    number = 7919;

    printf("Digite a quantidade de rounds que deseja executar: ");
    // scanf("%d", &rounds);

    rounds=20;

    MRA(number, rounds);

    return 0;
}