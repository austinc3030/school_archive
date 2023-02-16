import sys

from AES.ArgumentHandler import ArgumentHandler
from AES.ErrorHandler import ErrorHandler
from AES.Utilities import chunk_hex_string, convert_hex_to_binary, matricize_hex_string, \
                          split_hex_string, string_to_hex



class AES(object):

    def _obtain_initial_state(self):
        """
        Generates the initial state for the encryption operation
        """
        self.initial_state = matricize_hex_string(split_hex_string(string_to_hex(self.message)))


    def _add_key(self, subkey):
        """
        Generates the initial state for the encryption operation

        :param subkey: The subkey to use for the add_key round
        
        :return: The output of the add_key round
        """
        # TODO: CLEAN THIS UP
        subkey_matrix = matricize_hex_string(subkey)
        add_key_output = []

        for row_index in range(0, 4):
            row = []
            for column_index in range(0, 4):
                initial_state_element = convert_hex_to_binary(self.initial_state[row_index][column_index])
                subkey_element = convert_hex_to_binary(subkey_matrix[row_index][column_index])
                if len(initial_state_element) == len(subkey_element):
                    xor_result = ""
                    for bit_index in range(0, 8):
                        xor_result += str(int(bool(int(initial_state_element[bit_index])) ^
                                      bool(int(subkey_element[bit_index]))))
                row.append("{0:02x}".format(int(xor_result, 2)))
            add_key_output.append(row)

        return add_key_output


    def main(self):
        """
        The main method
        """
        self._obtain_initial_state()
        add_key_round_one_output=self._add_key(self.subkey0)  # Use Subkey0 for first round
        

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
            self.main()  # Start the main method
