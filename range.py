numbers = list(range(10))
print(numbers)
print(numbers[0])
print(numbers[4])

# If it is called with two arguments, it produces values from the first to the second.
num = list(range(3, 8))
print(num)
# Remember, the second argument is not included in the range, so range(3, 8) will not include the number 8.

print(range(20) == range(0, 20))

number1 = list(range(5, 20, 2))
# range can have a third argument, which determines the interval of the sequence produced, also called the step.
print(number1)

# We can also create list of decreasing numbers, using a negative number as the third argument,
# for example list(range(20, 5, -2)).
number2 = list(range(20, 5, -2))
print(number2)

# The for loop is commonly used to repeat some code a certain number of times.
# This is done by combining for loops with range objects.
for i in range(5):
    print("hello!")

