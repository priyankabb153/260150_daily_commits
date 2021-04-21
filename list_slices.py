"""
list slices

This returns a new list containing all the values in the old list between the indices.

"""

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

# Like the arguments to range, the first index provided in a slice is included
# in the result, but the second isn't.

#  If the first number in a slice is omitted, it is taken to be the start of the list.
print(squares[:7])

# If the second number is omitted, it is taken to be the end.
print(squares[7:])

# List slices can also have a third number, representing the step, to include only alternate values in the slice.
print(squares[::2])
print(squares[2:8:3])
# [2:8:3] will include elements starting from the 2nd index up to the 8th with a step of 3


#  When negative values are used for the first and second values in a slice (or a normal index),
#  they count from the end of the list.

print(squares[1:-1])

# If a negative value is used for the step, the slice is done backwards.
# Using [::-1] as a slice is a common and idiomatic way to reverse a list.

print(squares[::-1])

