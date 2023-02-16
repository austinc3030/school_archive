import sys

from AES.ArgumentHandler import ArgumentHandler
from AES.ErrorHandler import ErrorHandler
from AES.Utilities import initialize_state



class AES(object):

    def _obtain_initial_state(self):
        # Obtain initial state
        # Map each character to ascii
        # T  w  o     O  n  e     N  i  n  e     T  w  o
        # 54 77 6F 20 4F 6E 65 20 4E 69 6E 65 20 54 77 6F
        # Initialize State (4 by 4 array of bytes) with message
        # Divide into 4 parts
        # 54776F20    4F6E6520    4E696E65       2054776F
        # State should be
        # 54  4F  4E  20
        # 77  6E  69  54
        # 6F  65  6E  77
        # 20  20  65  6F

        state = initialize_state(self.message) 
        print(state)


    def main(self):
        self._obtain_initial_state()


    def __init__(self):
        self.error_handler = ErrorHandler()
        self.argument_handler = ArgumentHandler(error_handler=self.error_handler)
        if self.argument_handler.handle_arguments():
            self.message = self.argument_handler.message_to_encrypt
            self.subkey0 = self.argument_handler.subkey0
            self.subkey1 = self.argument_handler.subkey1
            self.main()
