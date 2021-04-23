# Write a Python program to find the repeated items of a tuple

"""
def find_repeat(tup):
    for i in range(len(tup)):
        print()
        # print(str(tup.count(tup[i]))+" "+str(i)+" "+str(tup[i]))
        if tup.count(tup[i]) > 1:
            print(tup[i])


# print(tuple1.count(2))

tuple1 = (1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 2, 3, 4, 2, 3, 2, 1)

# print("hello "+str(tuple1.count(6)))
find_repeat(tuple1)


"""
tuple1 = (1, 2, 3, 4, 5, 6, 7, 2, 3, 4, 5, 2, 3, 4, 2, 3, 2, 1)
print(tuple1)
n = int(input("enter a number to know how many times it repeated in the tuple"))
x = tuple1.count(n)
if x == 0:
    print(" the number u enetered is not present in the tuple")
elif x == 1:
    print("the number is not repeated ")
else:
    print("Repeates = "+str(x))



