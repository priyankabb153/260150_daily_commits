"""
Function Arguments


Python allows to have function with varying number of arguments.
Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function. The arguments are then accessible as the tuple args in the body of the function.
Example:


"""

def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1,2,3,4,5)

def func(x,y,food="spam"):
    print(food)

func(1,2)
func(3,4,"eggs")

# In case the argument is passed in, the default value is ignored.
# If the argument is not passed in, the default value is used.

def my_func(x,y=7,*args,**kwargs):
    print(kwargs)

my_func(2,3,4,5,6,a=7,b=8)

# The keyword arguments return a dictionary in which the keys are the argument names,
# and the values are the argument values.
# a and b are the names of the arguments that we passed to the function call.
# The arguments returned by **kwargs are not included in *args
