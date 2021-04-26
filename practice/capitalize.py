#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s

    # list = s.split(" ")
    # print(list)
    # print(s)
    # s[0]=s[0].upper()
    # for i in range(len(s)):
    # if s[i]==" ":
    # s[i+1]=s[i+1].upper()
    # print(i)
    # s[0].upper


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()