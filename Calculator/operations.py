from aux import get_polynomn 

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
    print('Multiplicação')
    return




def divide(n1, n2):
    print('Divisão')
    return


