# a list comprehension
# List comprehensions are a useful way of quickly creating lists whose contents obey a simple rule.

cubes = [i**3 for i in range(5)]
print(cubes)

evens = [i**2 for i in range(10) if i**2 % 2 ==0]

print(evens)


"""
Trying to create a list in a very extensive range will result in a MemoryError.
This code shows an example where the list comprehension runs out of memory.

"""
even = [2*i for i in range(10**100)]