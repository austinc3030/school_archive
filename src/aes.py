#!/usr/bin/python3
import sys
import argparse



def pre_main():

    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)
        
    try:
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

    except Exception as e:

        print(e)


if __name__ == '__main__':
    pre_main()