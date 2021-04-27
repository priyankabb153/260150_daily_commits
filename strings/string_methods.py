# capitalize
# Demonstrating the capitalize() method:
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# adding some spaces before and after the string.== center()

print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')

print('[' + 'gamma'.center(20, '*') + ']')

# The endswith() method
# checks if the given string ends with the specified argument and returns True or False,
# depending on the check result.

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# The find() method
#  it looks for a substring and returns the index of first occurrence of this substring,

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

print('kappa'.find('a', 2))

# You can use the find() method to search for all the substring's
# occurrences, like here:

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)


print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))


# The isalnum() method
# checks if the string contains only digits or alphabetical characters (letters),
# and returns True or False according to the result.

# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

# The isalpha() method
# Example 1: Demonstrating the isapha() method:
print("Moooo".isalpha())
print('Mu40'.isalpha())

# The isdigit() method
# Example 2: Demonstrating the isdigit() method:
print('2018'.isdigit())
print("Year2019".isdigit())

# The islower() method
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())

# The isspace() method
# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# The isupper() method
# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# The join() method
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# The lower() method
#  the source string remains untouched.
# Demonstrating the lower() method:
print("SiGmA=60".lower())

# The lstrip() method
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip("org"))

print("pythoninstitute.org".lstrip("pyth"))

# The replace() method
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# The rfind() method
# start their searches from the end of the string,
# not the beginning (hence the prefix r, for right).
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# The rstrip() method
# Two variants of the rstrip() method do nearly the same as lstrips,
# but affect the opposite side of the string.
# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
print("cisco.com".rstrip("cis"))

# The split() method
# splits the string and builds a list of all detected
# substrings.
# Demonstrating the split() method:
print("phi       chi\npsi".split())

# The startswith() method
# checks if a given string starts with the specified substring.
# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

# The strip() method
# The strip() method combines the effects caused by rstrip() and lstrip() - it makes a new string
# lacking all the leading and trailing whitespaces.

print()

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")

# The swapcase() method
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

print()

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

print()

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())

str = "emma watson"
print(str.title())


