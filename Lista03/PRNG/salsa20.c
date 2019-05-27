#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define ROUNDS 20


void salsa20_block(uint32_t out[16], uint32_t const in[16])
{
	int i;
	uint32_t x[16];

    // Faz uma matriz 16x16 com o input
	for (i = 0; i < 16; ++i) {
		x[i] = in[i];
        printf("\nx[%d] = %d", i, x[i] );
    }



}
int main(){
    unsigned char key[256];
    // unsigned char state[256];
    // int qtd=0;


    // printf("\n\n\n\n\nInsira uma chave de até 256 bits: ");
    // scanf("%s", key);

    uint32_t input=11111, output;

    salsa20_block(&output, &input);

    printf("\n\n%ld\n\n", output);


    return 0;
}