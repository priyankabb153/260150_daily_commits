"""
Recursion


Recursion is a very important concept in functional programming.
The fundamental part of recursion is self-reference - functions calling themselves.
 It is used to solve problems that can be broken up into easier sub-problems of the same type.

"""


def factorial(num):
    if num == 1:  # The base case acts as the exit condition of the recursion
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))

"""
def fact(x):
    return x * fact(x - 1)


print(fact(5))

"""


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

print(fib(4))