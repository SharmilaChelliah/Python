n=list(input())
n1=list(input())
flag=True
for i in n1:
    if i in n:
        n.remove(i)
    else:
        flag=False
if flag==True:
    print("YES")
else:
    print("NO")
