#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void KSA (unsigned char state[], unsigned char key[], int key_size){
    int i=0, j=0, temp=0;

    for (i=0; i < 256; i++){
        state[i] = i;
    }

    for (i=0; i < 256; ++i) {
        j = (j + state[i] + key[i % key_size]) % 256;
        temp = state[i];
        state[i] = state[j];
        state[j] = temp;
    }
}


void PRNG(unsigned char state[],int qtd){
    int i=0, j=0, temp=0, k=0;
    unsigned char character;

    FILE *outF = fopen("output_rc4.dat", "w");

    for (k=0; k < qtd; k++)  {
        i = (i + 1) % 256;
        j = (j + state[i]) % 256;
        temp = state[i];
        state[i] = state[j];
        state[j] = temp;

        character = state[(state[i] + state[j]) % 256];
        fputc(character, outF);
    }

    fclose(outF);
}

int main(){
    unsigned char key[256];
    unsigned char state[256];
    int qtd=0;


    printf("\n\n\n\n\nInsira uma chave de até 256 bits: ");
    scanf("%s", key);

    int key_size = strlen(key);

    KSA(state, key, key_size);


    printf("Insira a quantidade de bits que deseja gerar: " );
    scanf("%d", &qtd);

    PRNG(state, qtd);

    return 0;
}