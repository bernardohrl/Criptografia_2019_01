import os
from operations import add, subtract, multiply, divide
from aux import dec_to_binary, get_correct_number, get_correct_operation, check_values


def main():
    print('\nInsira o primeiro número: ', end='')
    n1 = get_correct_number(input())
    
    print('Insira o segundo número: ', end='')
    n2 = get_correct_number(input())

    print('\nSelecione entre as opções a seguir: ')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')
    print('Insira a opção desejada: ', end='')
    operacao = get_correct_operation(input())


    n1 = str(dec_to_binary(n1))
    n2 = str(dec_to_binary(n2))

    check_values(n1, n2, operacao)


    mapping = {
        1 : add,
        2 : subtract,
        3 : multiply,
        4 : divide
    }
    
    print('\n\nResultado: ')
    mapping[operacao](n1, n2)
    print('\n\n')


main()