#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void KSA (unsigned char state[], unsigned char key[], int key_size){
    int i=0, j=0, temp=0;

    for (i=0; i < 256; i++){
        state[i] = i;
    }

    // Shuffling
    for (i=0; i < 256; ++i) {
        j = (j + state[i] + key[i % key_size]) % 256;
        temp = state[i];
        state[i] = state[j];
        state[j] = temp;
    }
}


int main(){
    unsigned char key[256];
    unsigned char state[256];


    printf("Insira uma chave de até 256 bits: ");
    scanf("%s", key);

    int key_size = strlen(key);

    KSA(state, key, key_size);

    printf("\n\n%s\n\n", state);

    return 0;
}