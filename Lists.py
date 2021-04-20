# Lists are used to store items.
# A list is created using square brackets with commas separating items.
# A certain item in the list can be accessed by using its index in square brackets.
words = ["hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])


# An empty list is created with an empty pair of square brackets.
empty_file = []
print(empty_file)

# Typically, a list will contain items of a single item type,
# but it is also possible to include several different types.
# Lists can also be nested within other lists.
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[0])
print(things[2][2])
print(things[3])

# Nested lists can be used to represent 2D grids, such as matrices
m = [
    [1, 2, 3],
    [4, 5, 6]
]

print(m[0][2])

# Some types, such as strings, can be indexed like lists.
# Indexing strings behaves as though you are indexing a list
# containing each character in the string.

string = "hello world!"
print(string[3])
# Trying to access a non-existing index will produce an error.
# print(string[20])

# List Operations
# The item at a certain index in a list can be reassigned.
nums = [7, 7, 7, 7, 7]
nums[2] = 3
print(nums)


# Lists can be added and multiplied in the same way as strings.
print(nums + [1, 2, 3, 4, 5])
print(nums * 3)

# To check if an item is in a list, the in operator can be used.
# It returns True if the item occurs one or more times in the list,
# and False if it doesn't.
words = ["bread", "butter", "jam", "sos"]
print("bread" in words)
print("sos" in words)
print("sose" in words)
print("watch" in words)

if 7 in nums:
    print("available")

# The in operator is also used to determine whether
# or not a string is a substring of another string.

number = [1, 2, 3]
print(not 4 in number)
print(4 not in number)
print(not 3 in number)
print(3 not in number)

# The append method adds an item to the end of an existing list.
number.append([5, 6, 7])
# The dot before append is there because it is a method of the list class.
print(number)
# To get the number of items in a list, you can use the len function.
print(len(number))

# functions max,min,count,remove,reverse
list = [2,4,6,8,10]
print(list)
print(max(list))
print(min(list))
list.append(2)
list.insert(3,10)
list.insert(0,10)
print(list)
print(list.count(2))
print(list.count(10))
list.remove(10)
print(list)
list.reverse()
print(list)

# The insert method is similar to append, except that it allows you to insert a new item at any position in the list, as opposed to just at the end.
words = ["python","fun"]
#index = 1
words.insert(1,"is")
print(words)

letters = ['p', 'q', 'r', 's','p','u']
print(letters.index('r'))
# The index method finds the first occurrence of a list item and returns its index.
print(letters.index('p'))

# If the item isn't in the list, it raises a ValueError.
# print(letters.index('z'))

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
# 8