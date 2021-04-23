# Write a Python program to convert a list into a nested dictionary of keys

list1 = [1, 2, 3]
# list2 = ["MON", "TUE", "WED"]
# my_dict = {"John": 80, "Chauhan": 90, "Scott": 50}

my_dict = new = {}
for name in list1:
    new[name] = {}
    new = new[name]

print(my_dict)
