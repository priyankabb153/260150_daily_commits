"""
try/except statement
The try block contains code that might throw an exception.
If that exception occurs, the code in the try block stops being executed, and the code in the except block is run.
If no error occurs, the code in the except block doesn't run.
"""

try:
    num1 = 7
    num2 = 0
    print(num1/num2)
    print("done calculation")

except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")
except (ValueError, TypeError):
    print("Error occurred")
except:
    print("except to catch all the errors")

# example 1
try:
    num1 = input(":")
    num2 = input(":")
    print(float(num1)/float(num2))
except:
    print("Invalid input")
