"""
map


The built-in functions map and filter are very useful higher-order functions
 that operate on lists (or similar objects called iterables).
The function map takes a function and an iterable as arguments,
 and returns a new iterable with the function applied to each argument.
"""


def add_five(x):
    return x+5


nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

result = list(map(lambda x: x+5, nums))
print(result)

multiply = list(map(lambda x: x*2, nums))
print(multiply)

"""
filter


The function filter filters an iterable by removing items that
 don't match a predicate (a function that returns a Boolean).

"""

result = list(filter(lambda x : x%2 == 0, nums))
print(result)

result = list(filter(lambda x: x < 20, nums))
print(result)
# 11 is the only number less than 2
