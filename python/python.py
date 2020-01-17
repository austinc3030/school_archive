import sys

# Receive arguments
arg1 = sys.argv[1]


def handler(message):
    return message + "success"

print(handler(arg1))
sys.stdout.flush()
