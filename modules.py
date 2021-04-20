import random
import math
from math import pi
# from math import * # imports everthing
# the random module to generate random numbers:

for i in range(5):
    value = random.randint(1, 6)
    print(value)

# The code uses the randint function defined in the random module to print 5 random numbers in the range 1 to 6.

num = 10
print(math.sqrt(num))

print(pi)

# Trying to import a module that isn't available causes an ImportError.

"""
from math import sqrt as square_root
print(square_root(100))
"""

"""
Some of the standard library's useful modules include string,
 re, datetime, math, random, os, multiprocessing, subprocess, 
 socket, email, json, doctest, unittest, pdb, argparse and sys.
"""

"""
Many third-party Python modules are stored on the Python Package Index (PyPI).
enter pip install library_name. 
It's important to enter pip commands at the command line, not the Python interpreter.
"""