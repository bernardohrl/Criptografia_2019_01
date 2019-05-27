#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define ROUNDS 20


static uint32_t rotl(uint32_t value, int shift)
{
  return (value << shift) | (value >> (32 - shift));
}
 
void quarter_round(uint32_t a, uint32_t b, uint32_t c, uint32_t d) {
    b ^= rotl(a + d, 7);
    printf("\n\n%ld", b);
	c ^= rotl(b + a, 9);
    printf("\n%ld", b);
	d ^= rotl(c + b,13);
    printf("\n%ld", b);
	a ^= rotl(d + c,18);
    printf("\n%ld", b);
}

void salsa20_block(uint32_t out[16], uint32_t const in[16])
{
	int i;
	uint32_t x[16];

    // Faz uma matriz 16x16 com o input
	for (i = 0; i < 16; ++i) {
		x[i] = in[i];
        printf("\nx[%d] = %d", i, x[i]);
    }

    for (i = 0; i < ROUNDS; i += 2) {
		// Impar
		quarter_round(x[ 0], x[ 4], x[ 8], x[12]);
		quarter_round(x[ 5], x[ 9], x[13], x[ 1]);
		quarter_round(x[10], x[14], x[ 2], x[ 6]);
		quarter_round(x[15], x[ 3], x[ 7], x[11]);
		
        // Par
		quarter_round(x[ 0], x[ 1], x[ 2], x[ 3]);
		quarter_round(x[ 5], x[ 6], x[ 7], x[ 4]);
		quarter_round(x[10], x[11], x[ 8], x[ 9]);
		quarter_round(x[15], x[12], x[13], x[14]);
	}

    for (i = 0; i < 16; ++i) {
        out[i] = x[i] + in[i];
        printf("\nx[%d] = %d", i, out[i]);
    }
	


}


int main(){
    unsigned char key[256];
    // unsigned char state[256];
    // int qtd=0;


    // printf("\n\n\n\n\nInsira uma chave de até 256 bits: ");
    // scanf("%s", key);

    uint32_t input=11111, output[16];

    salsa20_block(output, &input);

    printf("\n\n%ld\n\n", output[2]);


    return 0;
}