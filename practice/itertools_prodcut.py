from itertools import product
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
#print(a)
#print(b)
print(list(product(a,b)))