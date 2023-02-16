import sys

from AES.AES import AES



if __name__ == '__main__':

    if sys.version_info<(3,5,0):
            sys.stderr.write("You need python 3.5 or later to run this script\n")
            sys.exit(1)
    else:
        aes = AES()
        if aes.error_handler.error_count > 0:
             print(aes.error_handler.exit_message)
        sys.exit(not(aes.error_handler.error_count == 0))