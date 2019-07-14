end_range = int(input())
prime_list = []
for i in range(3,end_range):
    flag = 0
    for j in range(2,i//2+1):
        if i%j == 0:
            flag = 1
    if flag == 0:
        prime_list.append(i)
stack = [2]
count = 0
for i in range(len(prime_list)):
    stack.append(prime_list[i])
    if sum(stack) in prime_list:
        count += 1
print(count)
