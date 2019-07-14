from itertools import groupby
a=input()
b=sorted(a)
for k,v in groupby(b):
    print(k,end="")
    print(len(list(v)),end="")
