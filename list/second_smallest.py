# Write a Python program to find the second smallest number in a list

list1 = [100, 200, 50, 25, 300, 500]
"""
n = len(list1)

sma = list1[0]
for i in range(len(list1)):
    if list1[i] < sma:
        sma = list1[i]


for i in range(n):
    #print(i)
    if list1[i] == sma:
       # print("sma")
        list1.remove(sma)
        break


#print(list1)

sma = list1[0]

for i in range(len(list1)):
    if list1[i] < sma:
        sma = list1[i]

print(sma)



"""

print(min(list1))
list1.remove(min(list1))
print(list1)
print(min(list1))



