n=int(input())
lst=input().split()
l1=""
l2=""
for i in range(0,len(lst),2):
    l1=l1+lst[i]
l1=sorted(l1)
for i in range(1,len(lst),2):
    l2=l2+lst[i]
l2=sorted(l2)
lst1=[]
j=1
k=1
lst1.insert(0,l1[0])
lst1.insert(1,l2[0])
for m in range(2,len(lst)):
    if m%2==0:
        lst1.insert(m,l1[j])
        j=j+1
    else:
        lst1.insert(m,l2[k])
        k=k+1
print(*lst1)
