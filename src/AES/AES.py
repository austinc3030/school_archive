import sys

from AES.ArgumentHandler import ArgumentHandler
from AES.ErrorHandler import ErrorHandler
from AES.Utilities import initialize_state



class AES(object):

    def _obtain_initial_state(self):
        self.initial_state = initialize_state(self.message)


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
