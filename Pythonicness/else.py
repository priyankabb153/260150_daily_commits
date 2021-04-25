# With the for or while loop, the code within it is called if the loop
# finishes normally (when a break statement does not cause an exit from the loop).

for i in range(10):
    if i == 999:
        break
else:
    print("Unbroken 1")

for i in range(10):
    if i ==5:
        break
else:
    print("Unbroken 2")

# The first for loop executes normally, resulting in the printing of "Unbroken 1".
# The second loop exits due to a break, which is why it's else statement is not executed.

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/10)
except ZeroDivisionError:
    print(4)
else:
    print(5)