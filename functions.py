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
