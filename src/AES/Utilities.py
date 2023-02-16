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


def chunk_message(message_to_chunk, number_of_chunks=4):
    # Initialize State (4 by 4 array of bytes) with message
    # Divide into 4 parts
    # 54776F20    4F6E6520    4E696E65       2054776F
    chunked_message = []

    split_message = split_hex_string(string_to_hex(message_to_chunk))
    chunk_length = int(len(message_to_chunk) / number_of_chunks)
    
    for message_index in range(0, number_of_chunks):
        message_chunk = []
        for chunk_index in range(0, chunk_length):
            message_chunk.append(split_message[message_index * chunk_length + chunk_index])
        chunked_message.append(message_chunk)
    
    return chunked_message


def initialize_state(message_for_state):
    # From the chunked message, it should go
    # 54776F20    4F6E6520    4E696E65       2054776F
    # Indexes              Example output
    # 00, 10, 20, 30       54  4F  4E  20
    # 01, 11, 21, 31 ____\ 77  6E  69  54
    # 02, 12, 22, 32     / 6F  65  6E  77
    # 03, 13, 23, 33       20  20  65  6F
    state = []

    chunked_message = chunk_message(message_to_chunk=message_for_state, number_of_chunks=4)
        
    for row_index in range(0, 4):
        row = []
        for column_index in range(0, 4):
            row.append(chunked_message[column_index][row_index])
        state.append(row)

    return state