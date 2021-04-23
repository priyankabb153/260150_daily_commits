# Write a Python program to convert a list of tuples into a dictionary


list1 = [("John", 80), ("Chauhan", 90), ("Scott", 50)]
my_dict = dict()

for key, val in list1:
    my_dict.setdefault(key, []).append(val)

print(my_dict)

print(dict(list1))

