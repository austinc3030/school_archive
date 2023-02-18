def convert_string_to_binary(string_to_convert):
    """
    Convert a string to binary character by character.

    :param string_to_convert: The string to convert to binary
    
    :return: The binary equivalent of the string
    """
    binary_result = ""

    for character in string_to_convert:
        binary_result += format(ord(character), '08b')

    return binary_result


def convert_hex_to_binary(string_to_convert):
    """
    Convert a hex string to binary hex number by hex number

    :param string_to_convert: The string to convert to binary
    
    :return: The binary equivalent of the string
    """
    binary_result = ""
    hex_number = ""

    for index, character in enumerate(string_to_convert):
        if len(hex_number) == 0:
            hex_number += character
        elif len(hex_number) == 1:
            hex_number += character

        # Need the or half of this condition to catch where the number of characters is odd
        if len(hex_number) == 2 or (index == len(string_to_convert) - 1):
            binary_result += format(int(hex_number, 16), '08b')
            hex_number = ""

    return binary_result


def string_to_hex(string_to_convert):
    """
    Convert a string to binary character by character.

    :param string_to_convert: The string to convert to binary
    
    :return: The binary equivalent of the string
    """
    hex_string = ""

    for character in string_to_convert:
        hex_string += "{0:02x}".format(ord(character))

    return hex_string


def split_hex_string(string_to_split):
    """
    Split a string of hex numbers to a list of hex numbers.
    
    :param string_to_split: The string to split
    
    :return: The split string
    """
    split_hex = []
    hex_number = ""

    for index, character in enumerate(string_to_split):
        if len(hex_number) == 0:
            hex_number += character
        elif len(hex_number) == 1:
            hex_number += character

        if len(hex_number) == 2:
            split_hex.append(hex_number)
            hex_number = ""

    return split_hex


def chunk_hex_string(string_to_chunk):
    """
    Split a string of hex numbers to a list of 4 hex numbers.
    
    :param string_to_chunk: The string to chunk
    
    :return: The chunked string
    """
    chunked_hex_string = []

    split_string = split_hex_string(string_to_chunk)
    
    for string_index in range(0, 4):
        string_chunk = []
        for chunk_index in range(0, 4):
            string_chunk.append(split_string[string_index * 4 + chunk_index])
        chunked_hex_string.append(string_chunk)
    
    return chunked_hex_string


def matricize_hex_string(hex_string_to_matricize):
    """
    Convert a string into a metrix where the indexes appear below

    0  4  8   12
    1  5  9   13
    2  6  10  14
    3  7  11  15

    :param hex_string_to_matricize: The string to matricize
    
    :return: The matrix of the hex string
    """
    matrix = []

    chunked_hex_string = chunk_hex_string(hex_string_to_matricize)
        
    for row_index in range(0, 4):
        row = []
        for column_index in range(0, 4):
            row.append(chunked_hex_string[column_index][row_index])
        matrix.append(row)

    return matrix


def hex_highbyte(hex_number):
    """
    Return the high byte of a hex number for lookup in the SBOX
    
    :param hex_number: The hex number to get the high byte from
    
    :return: The high_byte of the hex number
    """
    return (hex_number[0] + "0")


def hex_lowbyte(hex_number):
    """
    Return the low byte of a hex number for lookup in the SBOX
    
    :param hex_number: The hex number to get the low byte from
    
    :return: The low_byte of the hex number
    """
    return ("0" + hex_number[1])


def print_state(state):
    """
    Prints out the state given to the command line for viewing
    
    :param state: The state to output
    """
    print()
    for row in state:
        print(row)
    

def get_state_column(state, column_index):
    """
    Given a state, return an list that is the column index

    :param state: The state to return a column from
    :param column_index: The column index to return from the state
    
    :return: A list that is the column of the state
    """
    column = []
    for row_index, row in enumerate(state):
        column.append(state[row_index][column_index])
    
    return column


def convert_binary_to_polynomial(binary):
    """
    Given the binary number, convert it to a polynomial and return a list with the proper powers

    Format: [x8, x7, x6, x5, x4, x3, x2, x1, x0]

    :param binary: The binary number to convert

    :return: The polynomial as a list of the binary number
    """
    #                  x7     x6     x5     x4     x3     x2     x1     x0
    polynomial_list = [False, False, False, False, False, False, False, False]
    for bit_index, bit in enumerate(binary):
        if bit == "1":
            polynomial_list[bit_index] = True

    return polynomial_list


def convert_polynomial_to_boolean_list(polynomial):
    """
    Given a polynomial expression, convert it into binary
    
    :param polynomial: A polynomial expression to convert back to binary

    :return: the boolean list from the polynomial
    """
    #              x7     x6     x5     x4     x3     x2     x1     x0
    boolean_list = [False, False, False, False, False, False, False, False]
    
    if 7 in polynomial:
        boolean_list[0] = True
    if 6 in polynomial:
        boolean_list[1] = True
    if 5 in polynomial:
        boolean_list[2] = True
    if 4 in polynomial:
        boolean_list[3] = True
    if 3 in polynomial:
        boolean_list[4] = True
    if 2 in polynomial:
        boolean_list[5] = True
    if 1 in polynomial:
        boolean_list[6] = True
    if 0 in polynomial:
        boolean_list[7] = True
    
    return boolean_list


def convert_boolean_list_to_binary(boolean_list):
    """
    Given a boolean list, convert it to a binary number

    :param boolean_list: the boolean list to convert

    :return: The binary number
    """
    binary = ""

    for bit in boolean_list:
        binary += str(int(bit))

    return binary


def convert_binary_to_hex(binary_number):
    """
    Convert the given binary number to hex

    :param binary_number: the binary number to convert

    :return: The hex equivalent of the binary number
    """
    return "{:02x}".format(int(binary_number[0], 2))