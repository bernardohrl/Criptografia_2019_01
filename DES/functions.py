######################## KEY FUNCTIONS ####################################

def get_binary_key():
    with open('key.txt') as f:
        plain_key = f.read()

    plain_key = plain_key[:8]   # Deve ser no máximo 8 caracteres (64 bits)

    binary_key_64 = ''.join('{0:08b}'.format(ord(x), 'b') for x in plain_key)

    return str(binary_key_64)



def permutate_key(key_64bits):
    order = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    key_56bits = ""

    for index in order:
        key_56bits += key_64bits[index-1]

    # print('\n Permutated Key: ' + key_56bits)

    return key_56bits



def get_sub_key(key_56bits, number):

    # print("\n\n" + key_56bits)
    # print(str(len(key_56bits)))

    
    # Left Shift
    left = key_56bits[:28]
    right = key_56bits[28:]


    for _ in range(number):
        left = left[1:] + left[0]
        right = right[1:] + right[0]


    key_56bits = left + right


    # Reorder
    order = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
    key_48bits =  ''

    for index in order:
        key_48bits += key_56bits[index-1]

    # print('\n Permutated Key: ' + key_48bits)
    

    return key_48bits






