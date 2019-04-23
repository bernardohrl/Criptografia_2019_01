def dec_to_binary(text):
    binary_string = str(bin(int(text, 10))[2:].zfill(8))

    return binary_string


def get_correct_number(numero):
    
    while(int(numero) < 0 or int(numero) > 255):
        print('\nRange Inválido, escolha número entre 0 e 255')
        print('Insira novamente: ', end='')
        numero = input()

    return numero


def get_correct_operation(operacao):

    while(int(operacao) < 1 or int(operacao) > 4):
        print('\nEscolha entre as opções apresentadas (1 a 4).')
        print('Insira novamente: ', end='')
        operacao = input()

    return int(operacao)


def check_values(n1, n2, operacao):
    print('\n\nnum1: ' + n1)
    print('num2: ' + n2)
    print('opção: ' + str(operacao))