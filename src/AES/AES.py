from AES.ArgumentHandler import ArgumentHandler
from AES.ErrorHandler import ErrorHandler
from AES.SBox import SBox
from AES.Utilities import chunk_hex_string, convert_hex_to_binary, hex_highbyte, hex_lowbyte, matricize_hex_string, \
                          print_state, split_hex_string, string_to_hex



class AES(object):

    def _obtain_initial_state(self):
        """
        Generates the initial state for the encryption operation
        """
        return matricize_hex_string(split_hex_string(string_to_hex(self.message)))


    def _add_key(self, state, subkey):
        """
        Computes add_key based on the given state and subkey

        :param state: The current state to use for add_key
        :param subkey: The subkey to use for the add_key round
        
        :return: The output of the add_key round
        """
        # TODO: CLEAN THIS UP
        subkey_matrix = matricize_hex_string(subkey)
        
        for row_index in range(0, 4):
            for column_index in range(0, 4):
                state_element = convert_hex_to_binary(state[row_index][column_index])
                subkey_element = convert_hex_to_binary(subkey_matrix[row_index][column_index])
                if len(state_element) == len(subkey_element):
                    xor_result = ""
                    for bit_index in range(0, 8):
                        xor_result += str(int(bool(int(state_element[bit_index])) ^
                                      bool(int(subkey_element[bit_index]))))
                    state[row_index][column_index] = ("{0:02x}".format(int(xor_result, 2)))

        return state

    
    def _subbytes(self, state):
        """
        Uses SBox to substitute bytes in the current state with the values from SBOX

        :param state: The current state to use for sub_bytes
        
        :return: The output of the sub_bytes round
        """
        for row_index in range(0, 4):
            for column_index in range(0, 4):
                state_element = state[row_index][column_index]
                state_high_byte = hex_highbyte(state_element)
                state_low_byte = hex_lowbyte(state_element)
                state[row_index][column_index] = self.sbox[state_high_byte][state_low_byte]

        return state


    def _shiftrows(self, current_state):
        """
        Uses SBox to substitute bytes in the current state with the values from SBOX

        :param state: The current state to use for shift_rows
        
        :return: The output of the shift_rows round
        """
        shift_array = [[0, 1, 2, 3],
                       [1, 2, 3, 0],
                       [2, 3, 0, 1],
                       [3, 0, 1, 2]]

        new_state = []
        for row_index in range(0, 4):
            new_row = []
            for column_index in range(0, 4): 
                new_state_element = current_state[row_index][shift_array[row_index][column_index]]
                new_row.append(new_state_element)
            new_state.append(new_row)

        current_state = new_state

        return current_state


    def main(self):
        """
        The main method
        """
        initial_state = self._obtain_initial_state()
        current_state = self._add_key(initial_state, self.subkey0)  # Use Subkey0 for first round
        current_state = self._subbytes(current_state)
        current_state = self._shiftrows(current_state)

        print_state(current_state)
        

    def __init__(self):
        """
        During initialization of AES(), build the error handler, argument handler, and store the results
        from the argument handler in class variables
        """
        self.error_handler = ErrorHandler()
        self.argument_handler = ArgumentHandler(error_handler=self.error_handler)
        if self.argument_handler.handle_arguments():
            self.message = self.argument_handler.message_to_encrypt
            self.subkey0 = self.argument_handler.subkey0
            self.subkey1 = self.argument_handler.subkey1

            self.sbox = SBox().get_sbox()
            self.main()  # Start the main method
