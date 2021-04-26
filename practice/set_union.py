# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
eng_set={}
x=list(input().split())
french=int(input())
fre_set={}
y=list(input().split())
eng_set=set(x)
fre_set=set(y)
x = {}
#eng_set.update(fre_set)
#print(eng_set)
#print(fre_set)
#print(eng_set)
#print(fre_set)
print(len(eng_set.union(fre_set)))