import sys

from AES.ArgumentHandler import ArgumentHandler
from AES.ErrorHandler import ErrorHandler



class AES(object):        

    def main(self):
        pass

    def __init__(self):
        self.error_handler = ErrorHandler()
        self.argument_handler = ArgumentHandler(error_handler=self.error_handler)
        if self.argument_handler.handle_arguments():
            self.main()
