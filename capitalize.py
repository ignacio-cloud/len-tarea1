import math
import os
import random
import re
import sys


def solve(s):
    nombre = s.split(' ')
    return ' '.join((i.capitalize() for i in nombre))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
