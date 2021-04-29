multiline = '''Line #1
Line #2'''

print(len(multiline))

str1 = 'a'
str2 = 'b'

print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

# f you want to know a specific character's ASCII/UNICODE code point value,
# you can use a function named ord() (as in ordinal).

char_1 = 'a'
char_2 = ' '  # space

print(ord(char_1))
print(ord(char_2))

# The function takes a code point and returns its character.
print(chr(97))
print(chr(945))

# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# Iterating through a string.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# Slices

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

"""
 strings are immutable. 
 doesn't allow you to use the del instruction to remove anything from a string.
 The only thing you can do with del and a string is to remove the string as a whole.
 don't have the append() method
 the insert() method is illegal 

"""

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)


# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))

# t's an upper-case A.  the ASCII table - which letters occupy first locations - upper or lower=== upper

# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# finds the maximum element of the sequence.
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# its absence will cause a ValueError exception.

# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

