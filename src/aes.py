#!/usr/bin/python3
import sys
import argparse



def pre_main():

    if sys.version_info<(3,5,0):
        sys.stderr.write("You need python 3.5 or later to run this script\n")
        sys.exit(1)
        
    try:
        parser = argparse.ArgumentParser()

        parser.add_argument('--message', 'message', type=str, help='The message to encrypt', required=False)
        parser.add_argument('--subkey0', 'subkey0', type=str, help='The first subkey', required=False)
        parser.add_argument('--subkey1', 'subkey1', type=str, help='The second subkey', required=False)

        args=parser.parse_args()

        print(parser.print_help())

    except Exception as e:

        print(e)


if __name__ == '__main__':
    pre_main()