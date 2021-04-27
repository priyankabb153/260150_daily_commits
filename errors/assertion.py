import math

x = float(input("Enter a number: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

# The Python statement assert expression evaluates the expression and
# raises the AssertError exception when the expression is equal to
# zero, an empty string, or None. You can use it to protect some
# critical parts of your code from devastating data.

def foo(x):
    assert x
    return 1/x


try:
    print(foo(0))
except ZeroDivisionError:
    print("zero")
except:
    print("some")