"""
The finally statement is placed at the bottom of a try/except statement.
Code within a finally statement always runs after execution of the code
in the try, and possibly in the except, blocks.
"""

try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("done calculation")

except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")
finally:
    print("this code will run no matter what")

# Code in a finally statement even runs
# if an uncaught exception occurs in one of the preceding blocks.

print(1)
"""
raise ValueError
"""
# You can raise exceptions by using the raise statement.
print(2)

name = "123"
"""
  raise NameError("Invalid name!")
"""

try:
    num = 5/0
    
except:
    print("an error occurred")
    raise
