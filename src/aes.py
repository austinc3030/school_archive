#!/usr/bin/python3
import argparse
import os
import sys

# See progress at "work" to fill in pseudo code


class AES(object):

    def __init__(self):
        self.error_count = 0  # Indicates success
        self.exit_message = ""  # Empty exit message

        self.message_file = None
        self.subkey_file = None


    def _parse_args(self):
        parser = argparse.ArgumentParser()

        # Should take in the path to the message file
        parser.add_argument('--message-file', 
                            type=str, 
                            help='The path to the file containing the message '  # Help message is not hard-wrapped
                                 'to encrypt. Note: The message will be truncated to 128 bits.',
                            required=False)
        
        # Should take in the path to the file containing the subkeys
        parser.add_argument('--subkey-file',
                            type=str,
                            help='The path to the file containing the subkeys to '  # Help message is not hard-wrapped
                                 'be used for encryption. Note: Subkeys will be truncated to 128 bits.',
                            required=False)

        parsed_arguments=parser.parse_args()

        return parsed_arguments
    

    def _validate_args(self, parsed_arguments):
        # Validate message file exists
        if not os.path.isfile(os.path.abspath(parsed_arguments.message_file)):
            self.error_count += 1
            self.exit_message += 'Error {error_count}: --message-file "{message_file}" does not exist.\n' \
                                 .format(error_count=self.error_count, message_file=parsed_arguments.message_file)
        else:
            self.message_file = os.path.abspath(parsed_arguments.message_file)
        
        # Validate subkey file exists
        if not os.path.isfile(os.path.abspath(parsed_arguments.subkey_file)):
            self.error_count += 1
            self.exit_message += 'Error {error_count}: --subkey-file "{subkey_file}" does not exist.\n' \
                                 .format(error_count=self.error_count, subkey_file=parsed_arguments.subkey_file)
        else:
            self.subkey_file = os.path.abspath(parsed_arguments.subkey_file)

        return (self.message_file and self.subkey_file)


    def main(self):

        # Make sure we got valid args
        if self._validate_args(self._parse_args()):
            pass


if __name__ == '__main__':

    if sys.version_info<(3,5,0):
            sys.stderr.write("You need python 3.5 or later to run this script\n")
            sys.exit(1)
    else:
        aes = AES()
        aes.main()
        if aes.error_count > 0:
             print(aes.exit_message)
        sys.exit(not(aes.error_count == 0))