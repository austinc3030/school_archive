import sys
from pythontest import pytest2

# Receive arguments
arg1 = sys.argv[1]


def handler(message):
    return pytest2(message)

print(handler(arg1))
sys.stdout.flush()
