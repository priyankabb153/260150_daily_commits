"""
String formatting uses a string's format method to substitute a number of arguments in the string.
"""

# string formatting
nums = [4, 5, 6]
mgs = "numbers : {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(mgs)

a = "{x}, {y}".format(x=5, y=12)
print(a)
