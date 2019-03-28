import os
from functions import get_binary_key, permutate_key, get_sub_key

def main():

    # Clear Console
    os.system('cls' if os.name == 'nt' else 'clear')
    shifts_qtt = [1, 3, 5, 7, 9, 11, 13, 15, 16, 18, 20, 22, 24, 26, 28, 29]   # Quantidade de Shifts é acumulativa


    key_64bits = get_binary_key()
    key_56bits = permutate_key(key_64bits)



    print('Primeiramente, assegure-se de ter settar uma chave de até 8 caracteres no arquivo "key.txt"\n\n')

    print('Digite a mensagem: ', end="")
    plain_text = input()


    # Split in 64bits blocks
    plain_text_array = [plain_text[i:i+8] for i in range(0, len(plain_text), 8)]
    
    

    for index, block in enumerate(plain_text_array):
        print(block, index)

        for round in range(16):
            sub_key = get_sub_key(key_56bits, shifts_qtt[round])

            # print('\n Sub-Key[' + str(round+1) + ']:' + sub_key)

        
            
            # sub_key_2 = get_sub_key(key_56bits, shifts_qtt[round-1])

    print('\n')



    print("Mensagem: ")
    print("\t '" + plain_text + "'\n")

    print("Mensagem criptograda:")
    print("\t X\n")

    print("Mensagem Decriptografada: ")
    print("\t X\n")



    
    



main()
