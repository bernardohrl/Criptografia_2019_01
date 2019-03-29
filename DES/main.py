import os
import binascii
from encrypt_functions import initial_permutate_message_block, expand_function, xor, function, round_permutation, inverse_permutation
from key_functions import get_binary, permutate_key, get_sub_key


def main():

    # Get Keys
    with open('key.txt') as f:
        plain_key = f.read()
        plain_key = plain_key[:8]   # Deve ser no máximo 8 caracteres (64 bits)

    key_64bits = get_binary(plain_key)
    key_56bits = permutate_key(key_64bits)



    # Clear Console
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Primeiramente, assegure-se de ter settar uma chave de até 8 caracteres no arquivo "key.txt"\n\n')
    print('Digite a mensagem: ', end="")
    plain_text = input()



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
            
            right_expanded = expand_function(right)

            #RIGHT
            sub_key = get_sub_key(key_56bits, shifts_qtt[round])
            right_xor = xor(right_expanded, sub_key)

            right_6bits_array = [right_xor[i:i+6] for i in range(0, len(right_xor), 6)]            

            right_32bits = ''

            for right_6bits in right_6bits_array:
                right_32bits += function(right_6bits)

            rigth_permutated = round_permutation(right_32bits)

    
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
    



    print('\n')



    print("Mensagem: ")
    print("\t '" + plain_text + "'\n")

    print("Mensagem Criptograda:")
    print("\t" + chiper_text + "\n")

    print("Mensagem Decriptografada: ")
    print("\t X\n")



    
    



main()
