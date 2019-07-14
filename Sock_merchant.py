from collections import Counter
n=int(input())
lst=list(map(int,input().split()))
pair=0
inp=Counter(lst)
for i in inp.keys():
    if inp[i]==2:
        pair=pair+1
        flag=0
    elif inp[i]>=3:
        flag=0
        if inp[i]%2==0:
            c=inp[i]//2
            pair=pair+c
        else:
            e=inp[i]//2
            pair=pair+e
    else:
        flag=1
print(pair)
