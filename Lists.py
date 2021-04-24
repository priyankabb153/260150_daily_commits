# Lists are used to store items.
# A list is created using square brackets with commas separating items.
# A certain item in the list can be accessed by using its index in square brackets.

"""
Lists

1. The list is a type of data in Python used to store multiple objects.
 It is an ordered and mutable collection of comma-separated items between square brackets,
"""


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

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

# You should get the same sequence, but in reverse order
# (this is the merit of using the insert() method).

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)


# swapping with 3rd variable
# variable_1 = 1
# variable_2 = 2

# auxiliary = variable_1
# variable_1 = variable_2
# variable_2 = auxiliary

# swapping without 3rd variable

# variable_1 = 1
# variable_2 = 2
#
# variable_1, variable_2 = variable_2, variable_1

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)


my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

# 4. List elements and lists can be deleted, e.g.:

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

my_list = [8, 10, 6, 2, 4]
print(my_list)


for i in my_list:
    for i in range(len(my_list)-1):
        if my_list[i] > my_list[i+1]:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print()
print(my_list)

# or

my_list = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)

while swapped:
    swapped = False
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("\nSorted:")
print(my_list)



my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)


"""
The assignment: list_2 = list_1 copies the name of the array, not its contents. 
In effect, the two names (list_1 and list_2) identify the same location in the computer memory. 
Modifying one of them affects the other, and vice versa.

The program:

creates a one-element list named list_1;
assigns it to a new list named list_2;
changes the only element of list_1;
prints out list_2.
The surprising part is the fact that the program will output: [2], not [1], 
which seems to be the obvious solution.

"""

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)


# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# end is the index of the first element not included in the slice.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)



# If the start specifies an element lying further than the one
# described by the end (from the list's beginning point of view),
# the slice will be empty:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)


# The snippet's output is: []

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

# This is why its output is: [10, 8, 6].

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)


# Its output is therefore: [4, 2].

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# The snippet's output is: [10, 4, 2].

# Deleting all the elements at once is possible too:

my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)


# The list becomes empty, and the output is: [].
try:
    del my_list
    print(my_list)
except:
    print("runtime error.")

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Element found at index", i)
else:
    print("absent")

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)

# board = []
#
# for i in range(8):
#     row = [EMPTY for i in range(8)]
#     board.append(row)

EMPTY = "-"
ROOK = "ROOK"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

print(board)

temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "days were hot.")

# Three-dimensional arrays\

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# Now you can book a room for two newlyweds:
# in the second building, on the tenth floor, room 14:

rooms[1][9][13] = True

#and release the second room on the fifth floor located in the
# first building:

rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor
# of the third building:

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'


nums = [1,2,3]
vals = nums
del vals[1:2]
print(len(nums))
print(len(vals))

# my_list = [0,1,2,3]
# x=1
# for el in my_list:
#     x*= el
# print(x)
#
# vals = [1,2,3]
# vals = nums
# vals[0], vals[1]=vals[1],vals[2]
# print(len(vals))

my_list1 = [1,2,3,4]
print(my_list1[-3:-2])
# for v in range(len(my_list1)):
#     my_list1.insert(1,my_list1[v])
# print(my_list1)

x =1
x=x==x
print(x)

for i in range(1):
    print("#")
else:
    print("#")

vals = [0,1,2]
vals.insert(0,1)
del vals[1]
print(vals)

# li=[[0,1,2,3] for i in range(2)]
# print(li[2][0])

li = [i for i in range(-1,2)]
print(li)

z=10
y=0
x=y<z and z>y or y>z and z,y
print(x)

nums = [1,2,3]
vals = nums[-1:-2]
print(len(vals))
print(len(nums))

var =1
while var<10:
    print("#")
    var = var<<1

vals = [0,1,2]
vals[0], vals[2]=vals[2],vals[0]
print(vals)

i = 0
while i<=5:
    i+=1
    if i %2==0:
        break
    print("*")


t = [[3-i for i in range(3)]  for j in range(3)]
s=0
for i in range(3):
    s+=t[i][i]
print(s)
