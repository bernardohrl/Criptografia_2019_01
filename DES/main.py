import os
import binascii
from encrypt_functions import initial_permutate_message_block, expand_function, xor, function, round_permutation, inverse_permutation
from key_functions import get_binary, permutate_key, get_sub_key


def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    print('Primeiramente, assegure-se de ter settar uma chave de até 8 cara#cteres no arquivo "key.txt"\n\n')
    print('Digite a mensagem: ', end="")
    plain_text = input()



    print("\n\nMensagem: ")
    print("\t '" + plain_text + "'\n")



    key_56bits = get_56bits_key()
    chiper_text = encrypt(plain_text, key_56bits)

    print("\n\nMensagem Criptograda:")
    print("\t" + chiper_text + "\n")



    print("\nMensagem Decriptografada: ")
    print("\t X\n")




def get_56bits_key():
    
    with open('key.txt') as f:
        plain_key = f.read()
        plain_key = plain_key[:8]   # Deve ser no máximo 8 caracteres (64 bits)


    key_64bits = get_binary(plain_key)
    key_56bits = permutate_key(key_64bits)

    return key_56bits
    





def encrypt(plain_text, key_56bits):
    
    # Split into 8 letters block
    plain_text_array = [plain_text[i:i+8] for i in range(0, len(plain_text), 8)]


    # Shifts for encription
    shifts_qtt = [1, 3, 5, 7, 9, 11, 13, 15, 16, 18, 20, 22, 24, 26, 28, 29]   # Quantidade de Shifts é acumulativa
    chiper_text = ''


    for index, block in enumerate(plain_text_array):


        binary_block = get_binary(block)
        initial_permutated = initial_permutate_message_block(binary_block)


        left = initial_permutated[:32]
        right = initial_permutated[32:]



        for round in range(16):

            #Expand 
            right_expanded = expand_function(right)

            #XOR
            sub_key = get_sub_key(key_56bits, shifts_qtt[round])
            right_xor = xor(right_expanded, sub_key)


            # Function  (48bits -> 32bits)
            right_6bits_array = [right_xor[i:i+6] for i in range(0, len(right_xor), 6)]            

            right_32bits = ''

            for right_6bits in right_6bits_array:
                right_32bits += function(right_6bits)


            # Permutation    
            rigth_permutated = round_permutation(right_32bits)

    
            # Swap
            temp = right 
            right = xor(rigth_permutated, left)
            left = temp


        reverse = right + left
        permutated_text = inverse_permutation(reverse)
        
        array = [permutated_text[i:i+8] for i in range(0, len(permutated_text), 8)]

        print(array)

        for number in array:
            chiper_text += chr(int(number, 2))
            print(chr(int(number, 2)))
    
    return chiper_text




main()
