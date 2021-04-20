i = 1
# A while loop is used to repeat a block of code multiple times.
while i <= 10:
    if i % 2 == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")

    i = i + 1

print("finished")
# str(x) is used to convert the number x to a string, so that it can be used for concatenation.

# while True is a short and easy way to make an infinite loop.
# we can break an infinite loop if some condition is met
i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("breaking")
        break

print("Finished")

# the continue statement stops the current iteration and continues with the next one.
i = 1
while True:
    print(i)
    i = i + 1
    if i == 3:
        print("skipping 3")
        continue

    elif i >= 10:
        break
