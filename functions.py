print("Hello world!")
range(2, 20)
str(12)
range(10, 20, 3)


# The words in front of the parentheses are function names,
# and the comma-separated values inside the parentheses are function arguments.

# you can create your own functions by using the def statement.
# the argument is defined inside the parentheses
def my_func(word):
    for i in range(3):
        print(word + "!")


my_func("hello")
my_func("world")


###############################
def print_sum_diff(x, y):
    print(x + y)
    print(x - y)


print_sum_diff(10, 5)


##################################
def swap(x, y):
    z = x
    x = y
    y = z
    print("x is " + str(x) + " y is " + str(y))


swap(5, 10)


# print("x is " + str(x) + " y is " + str(y))
# Function arguments can be used as variables inside the function definition.
# However, they cannot be referenced outside of the function's definition.
# This also applies to other variables created inside a function.

def maximum(x, y, z):
    """

    :param x: 1st number
    :param y: 2nd number
    :param z: 3rd number
    :return:
    """

    if x >= y and x >= z:
        return x
        print("this wont be printed")
    elif y >= z:
        return y
    else:
        return z


print(max(2, 3, 4))
maxi = maximum(2, 3, 4)  # function to find maximum of 3 numbers
print(maxi)

# octothrope used to comment

# functions as object
"""
Although they are created differently from normal variables, functions are just like any other kind of value.
They can be assigned and reassigned to variables, and later referenced by those names.

"""


def multiply(x, y):
    return x * y


a = 4
b = 7
operation = multiply
# the name operation can also be used to call the function.
print(operation(a, b))


# Functions can also be used as arguments of other functions.
def add(x, y):
    return x + y


def do_twice(func, x, y):
    """

    :param func:
    :param x:
    :param y:
    :return:
    """
    return func(func(x, y), func(x, y))


a = 5
b = 10

print(do_twice(add, a, b))


# As you can see, the function do_twice takes a function as its argument and calls it in its body.


def square(x):
    """

    :param x: square function
    :return: square of the function has to be returned
    """
    return x * x


def test(func, x):
    print(func(x))


test(square, 42)
