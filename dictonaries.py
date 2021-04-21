"""
Dictionaries


Dictionaries are data structures used to map arbitrary keys to values.
Lists can be thought of as dictionaries with integer keys within a certain range.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
"""

ages = {"dave": 24, "marry": 42, "john": 58 }
print(ages["dave"])
print(ages["marry"])

# Each element in a dictionary is represented by a key:value pair.

primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
}
try:
    print(primary["red"])
    print(primary["yellow"])

except:
    print("KeyError: 'yellow'")

# An empty dictionary is defined as {}.

"""
Only immutable objects can be used as keys to dictionaries.
Immutable objects are those that can't be changed.
So far, the only mutable objects you've come across are lists and dictionaries. 
Trying to use a mutable object as a dictionary key causes a TypeError.

"""

try:
    bad_dict = {
    [1, 2, 3]: "one two three"
   }
except:
    print("TypeError: unhashable type: 'list'")

squares = {1 : 1, 2 : 4, 3 : "error", 4: 16, }


squares[8] = 64
squares[3] = 9
print(squares)
print(1 in squares)
print(16 in squares)
print(20 not in squares)

# a new dictionary key can also be assigned a value,
# not just ones that already exist.

# A useful dictionary method is get. It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead ('None', by default).
# Example:

print(squares.get(2))
print(squares.get("orages"))
print(squares.get(1234, "not in dictonary"))


fib = {1: 1, 2: 1, 3: 2, 4: 3}
print((fib.get(4, 0)+fib.get(7, 5)))
# sol : 8 3+5

