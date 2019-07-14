import collections
n , d1 = list(map(int,input().split()))
list_input = list(map(int,input().split()))
d = collections.deque(list_input)
d.rotate(-d1)
print(*list(d))
