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

from math import sin, pi

print(sin(pi/2))

import math as m

print(m.sin(m.pi/2))

from math import pi as PI, sin as sine

print(sine(PI/2))
print()
print(dir(math))

for name in dir(math):
    print(name, end="\t")

from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

from random import random, seed

seed(0)

for i in range(5):
    print(random())

from random import randrange, randint

print(randrange(5), end=' ')
print(randrange(0, 5), end=' ')
print(randrange(0, 5, 1), end=' ')
print(randint(0, 5))

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

from platform import platform,machine,processor,system,version

print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(processor())
print(system())
print(version())

#print(platform(aliased = False, terse = False))

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)



