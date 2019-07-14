n , d1 = list(map(int,input().split()))
list_input = list(map(int,input().split()))
list_input.sort()
sum = 0
count = 0
for i in range(n):
    sum = sum + list_input[i]
    if sum <= d1:
        count = count + 1
print(count)
