b=int(input())
z=int(input())
l=list(input().split())
for i in range(0,len(l)):
    if l[i].isdigit()==False:
        print("Invalid Input")
        flg=0
        break
    else:
        flg=1
if(flg==1):
    for i in range(0,len(l)):
        b1=(int(l[i])%2)+(int(l[i])/2)
        b=b-b1
        if(b<int(l[i])):
            flag=0
            print("No")
            break
        else:
            flag=1
if(flag==1):
    print("Yes")
