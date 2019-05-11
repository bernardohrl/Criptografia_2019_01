from aux import get_polynomn, check_values, get_coeficient

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

    if(int(n2, 2) > int(n1, 2)):
        print('\n\tBase10')
        print('\t\tQuociente: 0')
        print('\t\tResto:     ' + str(int(n1, 2)))
        print('\n\tBase2')
        print('\t\tQuociente: 0')
        print('\t\tResto:     ' + n1)
        print('\n\tPolinômio')
        print('\t\tQuociente: 0')
        print('\t\tResto:     ' + get_polynomn(n1))

    else:
        coeficient = ['0']*8

        while(n1 >= n2):
            rest = ''

            index, multiplied = get_coeficient(n1, n2)        # Pega o index para alterar a lista 'coeficient'
            coeficient[-index-1] = '1'                        # Na matemática o coeficiente é decrescent


            # Faz o XOR do dividendo e divisor multiplicado
            for index_temp, byte in enumerate(n1):
                bite = int(n1[index_temp] != multiplied[index_temp])
                rest += str(bite)

            
            n1 = rest

        # Transforma array 'coeficient' em string
        coeficient = ''.join(coeficient)  


        print('\n\tBase10')
        print('\t\tQuociente: ' + str(int(coeficient, 2)))
        print('\t\tResto:     ' + str(int(n1, 2)))
        print('\n\tBase2')
        print('\t\tQuociente: ' + coeficient)
        print('\t\tResto:     ' + n1)
        print('\n\tPolinômio')
        print('\t\tQuociente: ' + get_polynomn(coeficient))
        print('\t\tResto:     ' + get_polynomn(n1))



    return


