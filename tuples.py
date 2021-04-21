"""
Tuples


Tuples are very similar to lists, except that they are immutable (they cannot be changed).
Also, they are created using parentheses, rather than square brackets.
"""

words = ("spam", "eggs", "sausages")
# can access using index
print(words[0])
# reassigning causes a TypeError
try:
    words[1] = "hello"
except:
    print("TypeError: 'tuple' object does not support item assignment")

# Like lists and dictionaries, tuples can be nested within each other.


# Tuples can be created without the parentheses, by just separating the values with commas.
my_tuple = "one", "two", "three"
print(my_tuple[1])

# An empty tuple is created using an empty parenthesis pair.

tpl = ()
print(tpl)

# Tuples are faster than lists, but they cannot be changed.
