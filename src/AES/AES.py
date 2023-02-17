from AES.ArgumentHandler import ArgumentHandler
from AES.Constants import Constants
from AES.ErrorHandler import ErrorHandler
from AES.Utilities import chunk_hex_string, convert_hex_to_binary, hex_highbyte, hex_lowbyte, get_state_column, \
                          matricize_hex_string, print_state, split_hex_string, string_to_hex



class AES(object):

    def _generate_sbox(self):
        """
        Build the sbox dictionary so elements can be referenced by their hexadecimal indexes
        """
        self.sbox = {}
        # Build SBox
        for y_int_index, y_hex_index in enumerate(self.Constants.SBOX_Y_AXIS):
            row_array = self.Constants.SBOX_ROW_ARRAY[y_int_index]
            hex_row = {}
            for x_int_index, x_hex_index in enumerate(self.Constants.SBOX_X_AXIS):
                hex_row[x_hex_index] = row_array[x_int_index]
            
            self.sbox[y_hex_index] = hex_row


    def _obtain_initial_state(self):
        """
        Generates the initial state for the encryption operation
        """
        return matricize_hex_string(split_hex_string(string_to_hex(self.message)))


    def _addkey(self, state, subkey):
        """
        Computes add_key based on the given state and subkey

        :param state: The current state to use for add_key
        :param subkey: The subkey to use for the add_key round
        
        :return: The output of the add_key round
        """
        # TODO: CLEAN THIS UP
        subkey_matrix = matricize_hex_string(subkey)
        
        for row_index, row in enumerate(state):
            for column_index, column in enumerate(row):
                state_element = convert_hex_to_binary(state[row_index][column_index])
                subkey_element = convert_hex_to_binary(subkey_matrix[row_index][column_index])
                if len(state_element) == len(subkey_element):
                    xor_result = ""
                    for bit_index, bit in enumerate(state_element):
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
        for row_index, row in enumerate(state):
            for column_index, column in enumerate(row):
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
        new_state = []
        for row_index, row in enumerate(current_state):
            new_row = []
            for column_index, column in enumerate(row): 
                new_state_element = current_state[row_index][self.Constants.SHIFT_ARRAY_MAP[row_index][column_index]]
                new_row.append(new_state_element)
            new_state.append(new_row)

        current_state = new_state

        return current_state


    def _mixcolumns(self, current_state):
        """
        Perform mixcolumns on the given current state
        Reference: https://www.youtube.com/watch?v=0VgCy9daNjo

        :param current_state: the state to perform mixcolumns on

        :return: the new state after the mixcolumns operation
        """
        new_state = []

        print_state(current_state)
        print()

        mix_column_calculations = []

        for current_state_row_index, current_state_row in enumerate(current_state):
            for current_state_column_index, current_state_column in enumerate(current_state_row):
                column = get_state_column(current_state, current_state_column_index)
                column_calculations = [(str(self.Constants.MIX_COLUMN[current_state_row_index][0]) + " * " + str(column[0])),
                                       (str(self.Constants.MIX_COLUMN[current_state_row_index][1]) + " * " + str(column[1])),
                                       (str(self.Constants.MIX_COLUMN[current_state_row_index][2]) + " * " + str(column[2])),
                                       (str(self.Constants.MIX_COLUMN[current_state_row_index][3]) + " * " + str(column[3]))]
                mix_column_calculations.append(column_calculations)

        print(mix_column_calculations)
        # [02 03 01 01]   [d4]   [??]
        # [01 02 03 01] * [bf] = [66]
        # [01 01 02 03]   [5d]   [81]
        # [03 01 01 02]   [30]   [e5]

        # ?? = (02 * d4) XOR (03 * bf) XOR (01 * 5d) XOR (01 * 30)
        # T = T1 XOR T2 XOR T3 XOR T4

        # T1 = (02 * d4)
        # Convert hex to binary 02 -> 00000010
        # Convert binary to polynomial
        #   x7 XOR   x6 XOR   x5 XOR   x4 XOR   x3 XOR   x2 XOR   x1 XOR   x
        # 0*x7 XOR 0*x6 XOR 0*x5 XOR 0*x4 XOR 0*x3 XOR 0*x2 XOR 1*x1 XOR 0*x0
        # = x (because there is only 1 for x1)

        # Convert hex to binary d4 -> 11010100
        # Convert binary to polynomial
        #   x7 XOR   x6 XOR   x5 XOR   x4 XOR   x3 XOR   x2 XOR   x1 XOR   x
        # 1*x7 XOR 1*x6 XOR 0*x5 XOR 1*x4 XOR 0*x3 XOR 1*x2 XOR 0*x1 XOR 0*x0
        # = x7 XOR x6 XOR x4 XOR x2 (because there are 1's in the polynomial for these)

        # T1 = (x) * (x7 XOR x6 XOR x4 XOR x2) (Distribute X)
        # T1 = x8 XOR x7 XOR x5 XOR x3

        # T2 = (03 * bf) = x8 XOR x7 XOR x6 XOR 1
        # T3 = (01 * 5d) = x6 XOR x4 XOR x3 XOR x2 XOR 1
        # T4 = (01 * 30) = x5 XOR x4

        # T = T1 XOR T2 XOR T3 XOR T4
        # = x8 XOR x7 XOR x5 XOR x3 XOR x8 XOR x7 XOR x6 XOR 1 XOR x6 XOR x4 XOR x3 XOR x2 XOR 1 XOR x5 XOR x4
        # Cancel out same polynomial degrees
        # T = x2 (Each duplicate power gets eliminated)

        # Convert polynomial to binary
        # 0*x7 XOR 0*x6 XOR 0*x6 XOR 0x4 XOR 0*x3 XOR 1*x2 XOR 0*x1 XOR 0*x0
        # NOTE x^0 is 1 (anything to power of 0 is 1)
        # 0        0        0        0       0        1        0        0
        # Convert to hex
        # 00000100 = 0x04

        # If final polynomial value T is in the form of >x7 (There is something to the power of 8)
        # T' = T XOR Polynomial
        # T' = T XOR x8 XOR x4 XOR x3 XOR x XOR 1


        current_state = new_state

        return new_state


    def main(self):
        """
        The main method
        """
        initial_state = self._obtain_initial_state()
        current_state = self._addkey(initial_state, self.subkey0)  # Use Subkey0 for first round
        current_state = self._subbytes(current_state)
        current_state = self._shiftrows(current_state)

        ### REMOVE LATER. ONLY FOR TESTING
        test_state = [["d4"],
                      ["bf"],
                      ["5d"],
                      ["30"]]
        current_state = test_state
        ### REMOVE LATER. ONLY FOR TESTING

        current_state = self._mixcolumns(current_state)

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

            self.Constants = Constants()
            self._generate_sbox()
            self.main()  # Start the main method
