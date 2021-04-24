# 1. Tuples are ordered and unchangeable (immutable) collections of data. They can be thought of as immutable lists.
# They are written in round brackets:

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

# my_tuple.append(10000)
# del my_tuple[0]
# my_tuple[1] = -10
# AttributeError: 'tuple' object has no attribute 'append'

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(my_tuple * 3)
print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

var = 123

t1 = (1, )
t2 = (2, )
t3 = (3, var)

t1, t2, t3 = t2, t3, t1

print(t1, t2, t3)

my_tuple_1 = 1,
print(type(my_tuple_1))    # outputs: <class 'tuple'>

my_tuple_2 = 1             # This is not a tuple.
print(type(my_tuple_2))    # outputs: <class 'int'>

my_tuple = (1, 2.0, "string", [3, 4], (5, ), True)
#my_tuple[2] = "guitar"  # The TypeError exception will be raised.

my_tuple = 1, 2, 3,
del my_tuple
#print(my_tuple)    # NameError: name 'my_tuple' is not defined

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>


# By the same fashion, when you want to convert an iterable to a list,
# you can use a Python built-in function called list():


tup = 1, 2, 3,
my_list = list(tup)
print(my_list)
print(type(my_list))    # outputs: <class 'list'>

# Complete the code to correctly use the count() method to find the
# number of duplicates of 2 in the following tuple.

tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # outputs: 4

tup = (1,) + (1,)
tup = tup+tup
print(len(tup))