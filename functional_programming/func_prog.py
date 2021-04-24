def apply_twice(func, arg):
    return func(func(arg))


def add_five(x):
    return x + 5


print(apply_twice(add_five, 10))
# The function apply_twice takes another function as
# its argument, and calls it twice inside its body.


# not pure, because it changed the state of some_list.
some_list = []


def impure(arg):
    some_list.append(arg)

"""
Pure Functions


Using pure functions has both advantages and disadvantages.
Pure functions are:
- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
- easier to run in parallel.
The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O, since this appears to inherently require side effects.
They can also be more difficult to write in some situations.
"""
