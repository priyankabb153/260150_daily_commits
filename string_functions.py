"""
String Functions


Python contains many useful built-in functions and methods to accomplish common tasks.
join - joins a list of strings with another string as a separator.
replace - replaces one substring in a string with another.
startswith and endswith - determine if there is a substring at the start and end of a string, respectively.
To change the case of a string, you can use lower and upper.
The method split is the opposite of join turning a string with a certain separator into a list.
"""

print(", ".join(["spam", "eggs", "ham"]))
# prints ==> spam, eggs, ham

print("Hello Me".replace("Me", "World"))
# prints Hello World

print("this is a sentence.".startswith("rcb"))
# prints True

print("this is a sentence.".endswith("sentence"))
# prints false as sentence. is not written

print("This is a sentence.".upper())
# prints THIS IS A SENTENCE.

print("THIS IS A SENTENCE.".lower())
# prints this is a sentence.

print("This is a sentence.".swapcase())
# prints upper to lower and vice versa

print("spam, eggs, ham.".split(", "))
# prints ['spam', 'eggs', 'ham.']

"""
Numeric functions

"""

print(min(1, 2, 3, 4, 5, 0, -20, -1))
print(max(1, 2, 3, 4, 5, 0, -20, -1))
print(abs(-99))
print(abs(42))
try:
    print(sum(1, 2, 3, 4, 5))
except:
    print("TypeError: sum() takes at most 2 arguments (5 given)")

print(sum([1, 2, 3, 4, 5]))

print(round(23.444))
print(round(23.12345566, 2))
# round(number,to digits)


"""
List Functions


Often used in conditional statements, all and any take a list as an argument, and return True if all or any (respectively) of their arguments evaluate to True (and False otherwise).
The function enumerate can be used to iterate through the values and indices of a list simultaneously.

"""

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("at least one is even")

for v in enumerate(nums):
    print(v)

# prints (0, 55)
# (1, 44)
# (2, 33)
# (3, 22)
# (4, 11)


