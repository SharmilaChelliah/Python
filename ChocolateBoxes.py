from itertools import combinations 
n=int(input())
l=[]
c=0
for i in range(n):
    a=int(input())
    l.append(a)
for j in combinations(l,2):
    if sum(j)%60==0:
        c=c+1
print(c)
