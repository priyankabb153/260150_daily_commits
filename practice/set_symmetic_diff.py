m = int(input())
m_set = set(map(int, input().strip().split()))
n = int(input())
n_set = set(map(int,input().strip().split()))
z = n_set.symmetric_difference(m_set)
# for x in z:
#     print(x)
print(*sorted(list(m_set.symmetric_difference(n_set))),sep='\n')
