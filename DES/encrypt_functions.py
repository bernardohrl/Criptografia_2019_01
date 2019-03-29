def initial_permutate_message_block(block):
    order = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

    permutated_block = ''
    
    for index in order:
        permutated_block += block[index-1]


    return permutated_block




def expand_function(block):
    order = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

    expanded_block = ''

    for index in order:
        expanded_block += block[index-1]

    return expanded_block


def xor(block, subkey):
    
    xor = int(block,2) ^ int(subkey,2) 

    xor = bin(xor)[2:].zfill(len(block))

    return xor


def function(block_6bits):

    matrix = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ]

    row = int(block_6bits[0] + block_6bits [5], 2)
    column = int(block_6bits[1:5], 2)

    value =  matrix[row][column]
    binary = "{0:04b}".format(value)

    return str(binary)



def round_permutation(block):
    order = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

    permutated_block = ''

    for index in order:
        permutated_block += block[index-1]

    return permutated_block




def inverse_permutation(block):
    order = [40 , 8 , 48 , 16 , 56 , 24 , 64 , 32, 39 , 7 , 47 , 15 , 55 , 23 , 63 , 31, 38 , 6 , 46 , 14 ,  54 , 22 , 62 , 30, 37 , 5 , 45 , 13 , 53 , 21 , 61 , 29, 36 , 4 , 44 , 12 , 52 , 20 , 60 , 28, 35 , 3 , 43 , 11 , 51 , 19 , 59 , 27,  34 , 2 , 42 , 10 , 50 , 18 , 58 , 26, 33 , 1 , 41 , 9 , 49 , 17 , 57 , 25]

    permutated_block = ''

    for index in order:
        permutated_block += block[index-1]

    return permutated_block
