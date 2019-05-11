import os


def main():

    os.system('cls' if os.name == 'nt' else 'clear')

    print('Primeiramente, assegure-se de ter settar uma chave de até 32 caracteres (em hexa) no arquivo "key.txt"\n\n')
    print('Digite a mensagem (em hexa): ', end="")
    plain_text = '0123456789abcdeffedcba9876543210'



    print("\n\nMensagem: ", end='')
    print("'" + plain_text + "'\n")
