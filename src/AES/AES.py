import sys

from AES.ArgumentHandler import ArgumentHandler
from AES.ErrorHandler import ErrorHandler
from AES.Utilities import chunk_hex_string, matricize_hex_string, split_hex_string, string_to_hex



class AES(object):

    def _obtain_initial_state(self):
        self.initial_state = matricize_hex_string(split_hex_string(string_to_hex(self.message)))


    def _add_key(self, subkey):
        subkey_matrix = matricize_hex_string(subkey)
        add_key_output = []

        for row_index in range(0, 4):
            row = []
            for column_index in range(0, 4):
                initial_state_element = self.initial_state[row_index][column_index]
                subkey_element = subkey_matrix[row_index][column_index]
                # XOR initial_state with subkey
                row.append(None) # XOR output
            add_key_output.append(row)

        return add_key_output


    def main(self):
        self._obtain_initial_state()
        add_key_round_one_output=self._add_key(self.subkey0)  # Use Subkey0 for first round
        

    def __init__(self):
        self.error_handler = ErrorHandler()
        self.argument_handler = ArgumentHandler(error_handler=self.error_handler)
        if self.argument_handler.handle_arguments():
            self.message = self.argument_handler.message_to_encrypt
            self.subkey0 = self.argument_handler.subkey0
            self.subkey1 = self.argument_handler.subkey1
            self.main()  # Start the main method
