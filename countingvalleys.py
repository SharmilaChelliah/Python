n=int(input())
sealevel=0
valley_count=0
for i in input():
    if i=='U':
        sealevel=sealevel+1
    elif i=='D':
        sealevel=sealevel-1
    if sealevel==0 and i=='U':
        valley_count=valley_count+1
print(valley_count)
