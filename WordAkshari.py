def last_letter_finder(s):
    return s[-1]
def first_letter_finder(s):
    return s[0]
def matcher(s1,s2):
    if last_letter_finder(s1) == first_letter_finder(s2):
        return True

input_list = input().split()
lister = []
flag = 0
flag1 = 0
for i in range(len(input_list)):
    flag1 = 0
    if flag == 1:
        lister = [] + l
        break
    flag = 0
    first_word = input_list[i]
    l1 = [] + input_list
    l = []
    while(len(l1) != 0 and flag1 == 0):
        l.append(first_word)
        l1.remove(first_word)
        if len(l) == len(input_list):
            if matcher(l[-1],l[0]):
                flag = 1
                break
            else:
                break
        for j in range(len(l1)):
            if matcher(l[-1],l1[j]) == True:
                first_word = l1[j]
                break
        flag1 = 1
print("The word order for this bullshit game is")
if len(lister) == 0:
    print(*l1)
else:
    prnt(*lister)
