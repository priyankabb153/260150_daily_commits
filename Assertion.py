"""
An expression is tested, and if the result comes up false, an exception is raised.
Assertions are carried out through use of the assert statement.
"""

print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)


# The assert can take a second argument that is passed to the
# AssertionError raised if the assertion fails.
temp = -10
assert (temp >= 0), "colder than absolute zero!"
