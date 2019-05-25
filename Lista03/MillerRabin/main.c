#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


long long mulmod(long long a, long long b, long long mod)
{
    long long x = 0,y = a % mod;
    while (b > 0)
    {
        if (b % 2 == 1)
            x = (x + y) % mod;
        
        y = (y * 2) % mod;
        b /= 2;
    }
    return x % mod;
}


long long modulo(long long base, long long exponent, long long mod)
{
    long long x = 1;
    long long y = base;
    while (exponent > 0)
    {
        if (exponent % 2 == 1)
            x = (x * y) % mod;

        y = (y * y) % mod;
        exponent = exponent / 2;
    }
    return x % mod;
}


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
        long long mod = modulo(randon, temp, number);

        // printf("\n\n\nMod: %lld\n\n\n", mod);

        while (temp != number - 1 && mod != 1 && mod != number - 1)
        {
            mod = mulmod(mod, mod, number);
            
            printf("\n\n\nMulMod: %lld\n\n\n", mod);

            temp *= 2;
        }
        if (mod != number - 1 && temp % 2 == 0)
        {
            printf("\n\t%lld é composto\n\n\n", number);
            return 0;
        }

    }


    printf("\n\t%lld é primo\n\n\n", number);
    return 0;
}



int main(){
    long long number;
    int rounds;

    printf("\n\n\nDigite o número que deseja saber se é primo: ");
    // scanf("%lld", &number);
    number = 7921;

    printf("Digite a quantidade de rounds que deseja executar: ");
    // scanf("%d", &rounds);

    rounds=20;

    MRA(number, rounds);

    return 0;
}