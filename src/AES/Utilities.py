def convert_string_to_binary(string_to_convert):
    binary_result = ""

    for character in string_to_convert:
        binary_result += format(ord(character), '08b')

    return binary_result


def convert_hex_to_binary(string_to_convert):
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
    hex_string = ""

    for character in string_to_convert:
        hex_string += "{0:02x}".format(ord(character))

    return hex_string


def split_hex_string(string_to_split):
    # Map each character to ascii
    # T  w  o     O  n  e     N  i  n  e     T  w  o
    # 54 77 6F 20 4F 6E 65 20 4E 69 6E 65 20 54 77 6F
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
    chunked_hex_string = []

    split_string = split_hex_string(string_to_chunk)
    
    for string_index in range(0, 4):
        string_chunk = []
        for chunk_index in range(0, 4):
            string_chunk.append(split_string[string_index * 4 + chunk_index])
        chunked_hex_string.append(string_chunk)
    
    return chunked_hex_string


def matricize_hex_string(hex_string_to_matricize):
    matrix = []

    chunked_hex_string = chunk_hex_string(hex_string_to_matricize)
        
    for row_index in range(0, 4):
        row = []
        for column_index in range(0, 4):
            row.append(chunked_hex_string[column_index][row_index])
        matrix.append(row)

    return matrix
