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


def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction("James", "Doe")
introduction("James")
introduction(first_name="William")


def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)


introduction()


def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)


s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(s, c, p_c)


def subtra(a, b):
    print(a - b)


subtra(5, b=2)  # outputs: 3

# subtra(a=5, 2)  Syntax Error

subtra(a=5, b=2)


def add_numbers(x, y=2, z=3):
    print(x + y + z)


add_numbers(x=1)


# return without an expression


def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


happy_new_year()
happy_new_year(False)


# return with an expression


def boring_function():
    return 123


x = boring_function()

print("The boring_function has returned its result. It's:", x)


# Don't forget this: if a function doesn't return a certain value
# using a return expression clause,
# it is assumed that it implicitly returns None.


# list as function argument
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s


print(list_sum([5, 4, 3]))


# print(list_sum(5)) TypeError: 'int' object is not iterable


# A list can be a function result, too, e.g.:


def strange_list_fun(n):
    strange_list = []

    for i in range(0, n):
        strange_list.insert(0, i)

    return strange_list


print(strange_list_fun(5))


#  a variable existing outside a function has a scope
#  inside the functions' bodies.


def my_function():
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)


# A variable existing outside a function has a scope inside the
# functions' bodies, excluding those of them which define a variable of the same name.


def my_function():
    global var
    var = 2
    print("Do I know that variable?", var)


var = 1
my_function()
print(var)

# The code now outputs:
#
# Do I know that variable? 2
# 2


"""
Using this keyword inside a function with the name (or names separated with commas)
 of a variable(s), forces Python to refrain from creating a new variable inside the function -
 the one accessible from outside will be used instead.
"""


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)


# The code's output is:
#
# Print #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [0, 1]
# Print #4: [2, 3]
# Print #5: [2, 3]

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# Print #1: [2, 3]
# Print #2: [2, 3]
# Print #3: [3]
# Print #4: [3]
# Print #5: [3]


"""
if the argument is a list, then changing the value of the corresponding 
parameter doesn't affect the list (remember: variables containing lists are stored 
in a different way than scalars),
but if you change a list identified by the parameter
(note: the list, not the parameter!), the list will reflect the change.


"""

var = 2
print(var)  # outputs: 2


def return_var():
    global var
    var = 5
    return var


print(return_var())  # outputs: 5
var = 2
print(var)  # output 2

"""
backslash (\) symbol is used. If you use it in Python code and end a line with it, it will tell Python to continue the
 line of code in the next line of code.
"""


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(352.5, 1.65))
