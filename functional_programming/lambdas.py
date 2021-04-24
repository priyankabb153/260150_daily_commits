# def my_func(f, arg):
#     return f(arg)
#
#
# my_func(lambda x: 2 * x * x, 5)

# The same is possible with functions, provided that they are created using lambda syntax.
# Functions created this way are known as anonymous.

"""
Lambdas


Lambda functions aren't as powerful as named functions.
They can only do things that require a single expression 
- usually equivalent to a single line of code.
"""


def polynomial(x):
    return x ** 2 + 5 * x + 4


print(polynomial(-4))

#lambda

print((lambda x: x**2 + 5*x + 4)(-4))

double = lambda x: x * 2
print(double(7))

print((lambda x: x*2)(7))

triple = lambda x: x*3
add = lambda x, y: x+y

print(add(triple(3),4))
