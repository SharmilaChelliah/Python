import math
n=int(input())
k=int(input())
c=0
if(k%2==0):
    for i in range(0,k+1,2):
        comb=math.factorial(n)//(math.factorial(i)*math.factorial(n-i))
        c=c+comb
elif(k%2!=0):
    for i in range(0,k,2):
        comb=math.factorial(n)//(math.factorial(i)*math.factorial(n-i))
        c=c+comb
print(c)
