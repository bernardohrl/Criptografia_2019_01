from aux import get_polynomn, check_values

def add(n1, n2):
    result = ''

    for index, byte in enumerate(n1):
        # print(n1[index], n2[index], int((n1[index] != n2[index])) )
        bite = int(n1[index] != n2[index])
        result += str(bite)


    print('\tBase10:    ' + str(int(result, 2)))
    print('\tBase2:     ' + result)
    print('\tPolinômio: ' + get_polynomn(result))
    
    return
    


def subtract(n1, n2):
    result = ''

    for index, byte in enumerate(n1):
        # print(n1[index], n2[index], int((n1[index] != n2[index])) )
        bite = int(n1[index] != n2[index])
        result += str(bite)


    print('\tBase10:    ' + str(int(result, 2)))
    print('\tBase2:     ' + result)
    print('\tPolinômio: ' + get_polynomn(result))
    
    return





def multiply(n1, n2):
    n1 = list(n1)
    n2 = list(n2)

    # Multiplicação de Arrays Comum
    multiplication_array = [0]*(len(n1)+len(n2)-1)

    for index1, bit1 in enumerate(n1):
        for index2, bit2 in enumerate(n2):
            multiplication_array[index1+index2] += int(bit1)*int(bit2)

    # print(str(multiplication_array))

    # Como a adição é equivalente a um XOR, então o coeficiente existe quando a soma é impar
    multiplied = ''
    for bit in multiplication_array:
        if(bit % 2 == 0):
            multiplied += '0'
        else:
            multiplied += '1'

    multiplied = multiplied.lstrip('0') 
    # print(multiplied)    
    

    # Redução
    irred = '100011011'

    while(len(multiplied) > 8):
        # print('\n\n\n')
        # print(multiplied)
        # print(irred)

        for index in range(0,9):
            bite = int(multiplied[index] != irred[index])    # Calcula o XOR
            temp = list(multiplied)                          # Tranforma em lista, pois em python arrays são imutaveis
            temp[index] = str(bite)                          # Substitui bite na posição 'intex'
            multiplied = ''.join(temp)                       # Volta para array

        # print(multiplied)

        multiplied = multiplied.lstrip('0')                  # Remove 0 da esquerda para próxima iteração

    result = multiplied.zfill(8)
    # print(result)
    
    print('\tBase10:    ' + str(int(result, 2)))
    print('\tBase2:     ' + result)
    print('\tPolinômio: ' + get_polynomn(result))

    return




def divide(n1, n2):
    print('Divisão')
    return


