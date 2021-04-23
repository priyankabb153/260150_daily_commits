# Write a Python program to change the position of every n-th value with the (n+1)th in a list

list1 = [1, 0, 3, 2, 5, 4]

"""
i=0
while i <= (len(list1)-1):
    temp = list1[i]
    list1[i] = list1[i + 1]
    list1[i + 1] = temp
    i = i + 2


"""


def position(list1):
    for i in range(0, len(list1), 2):
        list1[i], list1[i + 1] = list1[i + 1], list1[i]

    return list1


print(position(list1))
