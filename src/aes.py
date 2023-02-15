#!/usr/bin/python3
import sys
import argparse

# See progress at "work" to fill in pseudo code


class AES(object):

    def __init__(self):
        pass
    
    def _parse_args(self):
        parser = argparse.ArgumentParser()

        # Should take in the path to the message file
        parser.add_argument('--message-file', 'message-file', 
                            type=str, 
                            help='The path to the file containing the message '  # Help message is not hard-wrapped
                                'to encrypt. Note: The message will be truncated to 128 bits.',
                            required=False)
        
        # Should take in the path to the file containing the subkeys
        parser.add_argument('--subkey-file', 'subkey-file',
                            type=str,
                            help='The path to the file containing the subkeys to '  # Help message is not hard-wrapped
                                'be used for encryption. Note: Subkeys will be truncated to 128 bits.',
                            required=False)

        args=parser.parse_args()

        return args
    

    def _validate_args(self, parsed_args):
        # validate the paths and that the file exists
        # Once files are validated, the message and keys must be validated (and truncated if necessary)
        message_file = parsed_args[0]
        subkey_file = parsed_args[1]

        self.message = None
        self.subkey0 = None
        self.subkey1 = None


    def main(self):

        return_code = 0
        self._validate_args(self._parse_args())

        return return_code


if __name__ == '__main__':

    if sys.version_info<(3,5,0):
            sys.stderr.write("You need python 3.5 or later to run this script\n")
            sys.exit(1)
    else:
        sys.exit(AES.main())