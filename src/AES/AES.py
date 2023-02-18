from AES.ArgumentHandler import ArgumentHandler
from AES.Constants import Constants
from AES.ErrorHandler import ErrorHandler
from AES.Utilities import chunk_hex_string, convert_binary_to_polynomial, convert_boolean_list_to_binary, \
                          convert_hex_to_binary, convert_polynomial_to_boolean_list, hex_highbyte, hex_lowbyte, \
                          get_state_column, matricize_hex_string, print_state, split_hex_string, string_to_hex



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


    def _shiftrows(self, state):
        """
        Uses SBox to substitute bytes in the current state with the values from SBOX

        :param state: The current state to use for shift_rows
        
        :return: The output of the shift_rows round
        """
        new_state = []
        for row_index, row in enumerate(state):
            new_row = []
            for column_index, column in enumerate(row): 
                new_state_element = state[row_index][self.Constants.SHIFT_ARRAY_MAP[row_index][column_index]]
                new_row.append(new_state_element)
            new_state.append(new_row)

        return new_state


    def _generate_mixcolumns_calculations(self, state):
        """
        Given a state object, generate the per element calculation for the entire state. Combines the state with the 
        mixcolumns matrix to determine the calculations to make for each element

        :param state: the state to generate the columns from

        :return: THe calculations required for mixcolumns
        """
        mixcolumns_calculations = []

        for current_state_row_index, current_state_row in enumerate(state):
            for current_state_column_index, current_state_column in enumerate(current_state_row):
                column = get_state_column(state, current_state_column_index)
                column_calculations = []
                for column_index, element in enumerate(column):
                    calculation = [self.Constants.MIX_COLUMN[current_state_row_index][column_index],
                                   column[column_index]]
                    column_calculations.append(calculation)
                mixcolumns_calculations.append(column_calculations)

        return mixcolumns_calculations


    def _convert_calculations_to_binary(self, calculations):
        """
        Take the calculations required and convert the calculation elements to binary

        :param calculations: the calculations object to convert

        :return: The calculations object in binary format
        """
        for row_index, row in enumerate(calculations):
            for column_index, column in enumerate(row):
                for element_index, element in enumerate(column):
                    calculations[row_index][column_index][element_index] = convert_hex_to_binary(element)

        return calculations
    

    def _expand_to_polynomial_calculations(self, calculations):
        """
        Taking the calculations given, expand them from binary to polynomial format

        :param calculations: The calculations to expand

        :return: The expanded calculations
        """
        for row_index, row in enumerate(calculations):
            for column_index, column in enumerate(row):
                for element_index, element in enumerate(column):
                    calculations[row_index][column_index][element_index] = convert_binary_to_polynomial(element)
                    # Operand is now in format seen in convert_binary_to_polynomial
                    # [  x7,   x6,   x5,   x4,   x3,   x2,   x1,   x0]
                    # [Bool, Bool, Bool, Bool, Bool, Bool, Bool, Bool]

        return calculations
    

    def _reduce_powers_from_calculations(self, calculations):
        """
        For each element in the calculations, reduce to the lowest number of powers contained in the calculation
        
        :param calculations: the calculations to reduce powers from

        :return: the calculations with 0 powers removed
        """
        for row_index, row in enumerate(calculations):
            for column_index, column in enumerate(row):
                for operand_index, operand in enumerate(column):
                    new_calculation = []
                    if operand[0]:
                        new_calculation.append(7)
                    if operand[1] == True:
                        new_calculation.append(6)
                    if operand[2] == True:
                        new_calculation.append(5)
                    if operand[3] == True:
                        new_calculation.append(4)
                    if operand[4] == True:
                        new_calculation.append(3)
                    if operand[5] == True:
                        new_calculation.append(2)
                    if operand[6] == True:
                        new_calculation.append(1)
                    if operand[7] == True:
                        new_calculation.append(0)
                    calculations[row_index][column_index][operand_index] = new_calculation

        return calculations
    

    def _perform_multiplication_of_elements(self, calculations):
        """
        Given the calculations to make, perform the multiplcation (Addition of exponents)

        :param calculations: the calculations to make

        :return: The multipled calculations
        """
        for row_index, row in enumerate(calculations):
            for column_index, column in enumerate(row):
                left_element = column[0]
                right_element = column[1]
                # Perform left_element * right_element by distributing powers
                new_element = []
                for left_index, left in enumerate(left_element):
                    for right_index, right in enumerate(right_element):
                        new_element.append(left + right)
                calculations[row_index][column_index] = new_element

        return calculations
    

    def _substitute_eighth_powers(self, calculations):
        """
        Replace any eights powers with 8, 4, 3, 1, 0

        :param calculations: The calculations to replace substitute irreductible polynomial

        :return: The calculations with the eighth powers replaced
        """
        for row_index, row in enumerate(calculations):
            for column_index, column in enumerate(row):
                if 8 in column:
                    calculations[row_index][column_index].append(8)
                    calculations[row_index][column_index].append(4)
                    calculations[row_index][column_index].append(3)
                    calculations[row_index][column_index].append(1)
                    calculations[row_index][column_index].append(0)
        
        return calculations

    
    def _cancel_like_terms(self, calculations):
        """
        Cancel liked terms in the calculations
        
        :param calculations: The calculations to cancel like terms
        
        :return: Calculations with the like terms removed
        """
        for row_index, row in enumerate(calculations):
            for column_index, column in enumerate(row):
                new_calculation = []
                for element_index, element in enumerate(column):
                    if (column.count(element) % 2 ) != 0:  # ODD
                        new_calculation.append(element)
                calculations[row_index][column_index] = list(dict.fromkeys(new_calculation))
                
        return calculations


    def _cascade_calculations(self, calculations):
        """
        With all of the prep work done, cascade the calculations sideways to get the value for each
        element in the column
        
        :param calculations:

        :return: The calculations cascaded appropriately per column
        """
        new_calculations = []

        for row_index, row in enumerate(calculations):
            new_row = []
            for column_index, column in enumerate(row):
                new_column = []
                for element_index, element in enumerate(row):
                    new_column.extend(element)    
            new_row.append(new_column)
            new_calculations.append(new_row)

        return new_calculations
    

    def _convert_calculation_outputs_to_boolean_list(self, calculations):
        """
        Convert each element in the calculations object from a polynomial expression to a binary expression

        :param calculations: the calculations object to convert

        :return: The binary converted calculations
        """

        for row_index, row in enumerate(calculations):
            for column_index, column in enumerate(row):
                calculations[row_index][column_index] = convert_polynomial_to_boolean_list(column)

        return calculations

    
    def _convert_boolean_calculations_to_binary(self, boolean_calculations):
        """
        Convert the given boolean list into binary

        :param boolean_calculations: the calculations to convert to binary

        :return: The converted calculations
        """
        binary_calculations = []

        for row_index, row in enumerate(boolean_calculations):
            new_row = []
            for column_index, column in enumerate(row):
                new_column = []
                new_column.append(convert_boolean_list_to_binary(column))
                new_row.append(new_column)
            binary_calculations.append(new_row)

        return binary_calculations
    

    def _convert_binary_calculations_to_hex(self, binary_calculations):
        """
        Convert the binary calculations into hex output

        :param binary_calculations: the binary calculations to convert to hex

        :return: The hex output from the conversion
        """
        for row_index, row in enumerate(binary_calculations):
            for column_index, column in enumerate(row):
                binary_calculations[row_index][column_index] = 


    def _mixcolumns(self, state):
        """
        Perform mixcolumns on the given current state
        Reference: https://www.youtube.com/watch?v=0VgCy9daNjo

        :param current_state: the state to perform mixcolumns on

        :return: the new state after the mixcolumns operation
        """
        new_state = []

        print_state(state)
        print()

        mixcolumn_calculations = self._generate_mixcolumns_calculations(state)

        binary_calculations = self._convert_calculations_to_binary(mixcolumn_calculations)
        polynomial_calculations = self._expand_to_polynomial_calculations(binary_calculations)
        #print_state(polynomial_calculations)
        calculations_with_reduced_powers = self._reduce_powers_from_calculations(polynomial_calculations)
        #print_state(calculations_with_reduced_powers)
        multiplied_elements = self._perform_multiplication_of_elements(calculations_with_reduced_powers)
        #print_state(multiplied_elements)
        cancelled_terms_before_cascade = self._cancel_like_terms(multiplied_elements)
        #print_state(cancelled_terms_before_cascade)
        cascaded_calculations = self._cascade_calculations(cancelled_terms_before_cascade)
        #print_state(cascaded_calculations)
        cancelled_terms_after_cascade = self._cancel_like_terms(cascaded_calculations)
        #print_state(cancelled_terms_after_cascade)
        replaced_eighth_powers = self._substitute_eighth_powers(cancelled_terms_after_cascade)
        #print_state(replaced_eighth_powers)
        cancelled_terms_after_substitution = self._cancel_like_terms(replaced_eighth_powers)
        print_state(cancelled_terms_after_substitution)
        boolean_calculation_outputs = \
            self._convert_calculation_outputs_to_boolean_list(cancelled_terms_after_substitution)
        print_state(boolean_calculation_outputs)
        binary_output_of_boolean_list = self._convert_boolean_calculations_to_binary(boolean_calculation_outputs)
        print_state(binary_output_of_boolean_list)
        hex_output = self._convert_binary_calculations_to_hex(binary_output_of_boolean_list)

            

        #substituted_eighth_powers = self._substitute_eighth_powers(first_cancel)
        #print_state(substituted_eighth_powers)
        
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
