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

        self.message_file_contents = None
        self.subkey_file_contents = None

        self.raw_message_to_encrypt = None
        self.raw_subkey0 = None
        self.raw_subkey1 = None


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


    def _read_message_file(self):
        with open(self.message_file) as message_file:
            message_file_contents = list(filter(None, message_file.read().splitlines()))

            if len(message_file_contents) == 1:
                self.raw_message_to_encrypt = message_file_contents[0]
            elif len(message_file_contents) > 1:
                self.error_count += 1
                self.exit_message += 'Error {error_count}: --message-file "{message_file}" contains more than one ' \
                                    'message.\n'.format(error_count=self.error_count, message_file=self.message_file)
            else:
                self.error_count += 1
                self.exit_message += 'Error {error_count}: --message-file "{message_file}" is empty.\n' \
                                    .format(error_count=self.error_count, message_file=self.message_file)
        
        return (self.raw_message_to_encrypt)


    def _read_subkey_file(self):
        with open(self.subkey_file) as subkey_file:
            subkey_file_contents = list(filter(None, subkey_file.read().splitlines()))

            if len(subkey_file_contents) == 2:
                self.raw_subkey0 = subkey_file_contents[0]
                self.raw_subkey1 = subkey_file_contents[1]
            elif len(subkey_file_contents) > 2:
                self.error_count += 1
                self.exit_message += 'Error {error_count}: --subkey-file "{subkey_file}" contains more than two ' \
                                    'subkeys.\n'.format(error_count=self.error_count, subkey_file=self.subkey_file)
            elif len(subkey_file_contents) == 1:
                self.error_count += 1
                self.exit_message += 'Error {error_count}: --subkey-file "{subkey_file}" only contains one subkey.\n' \
                                    .format(error_count=self.error_count, subkey_file=self.subkey_file)
            else:
                self.error_count += 1
                self.exit_message += 'Error {error_count}: --subkey-file "{subkey_file}" is empty.\n' \
                                    .format(error_count=self.error_count, subkey_file=self.subkey_file)
        
        return (self.raw_subkey0 and self.raw_subkey1)


    def main(self):

        # Make sure we got valid args
        if self._validate_args(self._parse_args()):
            if self._read_message_file() and self._read_subkey_file():
                print("True")
            else:
                print("False")


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