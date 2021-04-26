n = int(input())
set1={}
list1=[]

for i in range(n):
    z=input()
    list1.append(z)
    #print(list1)

set1=set(list1)
print(len(set1))