import argparse
import os
import sys

from AES.Utilities import convert_string_to_binary, convert_hex_to_binary



class ArgumentHandler(object):

    def __init__(self, error_handler):
        self.error_handler = error_handler

        self.message_file = None
        self.subkey_file = None

        self.message_file_contents = None
        self.subkey_file_contents = None

        self.message_to_encrypt = None
        self.subkey0 = None
        self.subkey1 = None


    def _parse_args(self):
        parser = argparse.ArgumentParser()

        # Should take in the path to the message file
        parser.add_argument('--message-file', 
                            type=str, 
                            help='The path to the file containing the message '  # Help message is not hard-wrapped
                                 'to encrypt. Note: The message must be 128 bits.',
                            required=True)
        
        # Should take in the path to the file containing the subkeys
        parser.add_argument('--subkey-file',
                            type=str,
                            help='The path to the file containing the subkeys to '  # Help message is not hard-wrapped
                                 'be used for encryption. Note: Subkeys must be 128 bits.',
                            required=True)

        parsed_arguments=parser.parse_args()

        return parsed_arguments
    

    def _validate_args(self, parsed_arguments):
        # Validate message file exists
        if not os.path.isfile(os.path.abspath(parsed_arguments.message_file)):
            self.error_handler.error_count += 1
            self.error_handler.exit_message += 'Error {error_count}: --message-file "{message_file}" does not ' \
                                               'exist.\n'.format(error_count=self.error_handler.error_count,
                                                                 message_file=parsed_arguments.message_file)
        else:
            self.message_file = os.path.abspath(parsed_arguments.message_file)
        
        # Validate subkey file exists
        if not os.path.isfile(os.path.abspath(parsed_arguments.subkey_file)):
            self.error_handler.error_count += 1
            self.error_handler.exit_message += 'Error {error_count}: --subkey-file "{subkey_file}" does not ' \
                                               'exist.\n'.format(error_count=self.error_handler.error_count,
                                                                 subkey_file=parsed_arguments.subkey_file)
        else:
            self.subkey_file = os.path.abspath(parsed_arguments.subkey_file)

        return bool(self.message_file and self.subkey_file)


    def _read_message_file(self):
        with open(self.message_file) as message_file:
            message_file_contents = list(filter(None, message_file.read().splitlines()))

            if len(message_file_contents) == 1:
                self.message_to_encrypt = message_file_contents[0]
            elif len(message_file_contents) > 1:
                self.error_handler.error_count += 1
                self.error_handler.exit_message += 'Error {error_count}: --message-file "{message_file}" contains ' \
                                                   'more than one message.\n' \
                                                   .format(error_count=self.error_handler.error_count,
                                                           message_file=self.message_file)
            else:
                self.error_handler.error_count += 1
                self.error_handler.exit_message += 'Error {error_count}: --message-file "{message_file}" is empty.\n' \
                                    .format(error_count=self.error_handler.error_count, message_file=self.message_file)

        return bool(self.message_to_encrypt)


    def _read_subkey_file(self):
        with open(self.subkey_file) as subkey_file:
            subkey_file_contents = list(filter(None, subkey_file.read().splitlines()))

            if len(subkey_file_contents) == 2:
                self.subkey0 = subkey_file_contents[0]
                self.subkey1 = subkey_file_contents[1]
            elif len(subkey_file_contents) > 2:
                self.error_handler.error_count += 1
                self.error_handler.exit_message += 'Error {error_count}: --subkey-file "{subkey_file}" contains ' \
                                                   'more than two subkeys.\n' \
                                                   .format(error_count=self.error_handler.error_count,
                                                           subkey_file=self.subkey_file)
            elif len(subkey_file_contents) == 1:
                self.error_handler.error_count += 1
                self.error_handler.exit_message += 'Error {error_count}: --subkey-file "{subkey_file}" only ' \
                                                   'contains one subkey.\n' \
                                                   .format(error_count=self.error_handler.error_count,
                                                           subkey_file=self.subkey_file)
            else:
                self.error_handler.error_count += 1
                self.error_handler.exit_message += 'Error {error_count}: --subkey-file "{subkey_file}" is empty.\n' \
                                    .format(error_count=self.error_handler.error_count, subkey_file=self.subkey_file)
        
        return bool(self.subkey0 and self.subkey1)
    

    def _validate_message_length(self):
        if len(convert_string_to_binary(self.message_to_encrypt)) != 128:
            self.error_handler.error_count += 1
            self.error_handler.exit_message += 'Error {error_count}: Message "{message_to_encrypt}" is not exactly ' \
                                               '128 bits.\n'.format(error_count=self.error_handler.error_count,
                                                                    message_to_encrypt=self.message_to_encrypt)
            return False

        return True


    def _validate_subkey_length(self):
        if len(convert_hex_to_binary(self.subkey0)) != 128:
            self.error_handler.error_count += 1
            self.error_handler.exit_message += 'Error {error_count}: Subkey0 "{subkey0}" is not exactly ' \
                                               '128 bits.\n'.format(error_count=self.error_handler.error_count,
                                                                    subkey0=self.subkey0)
            return False
        
        if len(convert_hex_to_binary(self.subkey1)) != 128:
            self.error_handler.error_count += 1
            self.error_handler.exit_message += 'Error {error_count}: Subkey1 "{subkey1}" is not exactly ' \
                                               '128 bits.\n'.format(error_count=self.error_handler.error_count,
                                                                    subkey1=self.subkey1)
            return False

        return True
    

    def handle_arguments(self):

        if not self._validate_args(self._parse_args()):
            return False
        if not self._read_message_file():
            return False
        if not self._read_subkey_file():
            return False
        if not self._validate_message_length():
            return False
        if not self._validate_subkey_length():
            return False

        return True
