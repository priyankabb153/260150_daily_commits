"""
itertools

The function count counts up infinitely from a value.
The function cycle infinitely iterates through an iterable
 (for instance a list or string).
The function repeat repeats an object, either infinitely or a
 specific number of times.

takewhile - takes items from an iterable while a predicate function remains true;
chain - combines several iterables into one long one;
accumulate - returns a running total of values in an iterable.
"""

from itertools import count

for i in count(3):
    print(i)
    if i>=11:
        break


from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x:x<=6, nums)))

from itertools import takewhile

nums = [2,4,6,7,8,9]

a = takewhile(lambda x:x%2==0,nums)
print(list(a))

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters,range(2))))
print(list(permutations(letters)))
a={1,2}
print(len(list(product(range(3),a))))
print(list(product(range(3),a)))