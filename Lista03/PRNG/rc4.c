#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void KSA (unsigned char state[], unsigned char key[], int key_size){
    printf("%s", key);
    printf("\n\n");
    printf("key size: %i", key_size);
    printf("\n\n");
}


int main(){
    unsigned char key[256];
    unsigned char state[256];


    printf("Insira uma chave de até 256 bits: ");
    scanf("%s", key);

    int key_size = strlen(key);

    KSA(state, key, key_size);

    return 0;
}