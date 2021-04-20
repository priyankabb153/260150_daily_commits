# The for loop is used to iterate over a given sequence, such as lists or strings.

words = ["monday", "tuesday", "wednesday", "thursday"]
for word in words:
    print(word+"!")

string = "testing for loops"
print(string.count('t'))

cnt = 0
for x in string:
    if x == 't':
        cnt += 1

print(cnt)

# Similar to while loops, the break and continue statements can be used in for loops,
# to stop the loop or jump to the next iteration.

# It is common to use the for loop when the number of iterations is fixed.
# For example, iterating over a fixed list of items in a shopping list.
# The while loop is used in cases when the number of iterations is not known and depends on some
# calculations and conditions in the code block of the loop.
# For example, ending the loop when the user enters a specific input in a calculator program.
