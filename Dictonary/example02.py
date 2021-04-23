my_dict = {"one": [10, 20, 30], "two": [40, 50, 60]}

print(my_dict)

for k, val in my_dict.items():
    print(k, val)

print()

for k in my_dict:
    print(my_dict[k])

print(my_dict["two"][0])
print(my_dict["two"][1])
print(my_dict["two"][2])