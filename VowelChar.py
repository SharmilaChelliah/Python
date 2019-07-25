input_string=input()
inp_list=list(input_string)
dup_list=inp_list[:]
empty_list=[]
list_len=len(dup_list)
vowels=['a','e','i','o','u']
for i in range(0,list_len):
    if dup_list[i] in vowels:
        if i==0:
            empty_list.append(inp_list[i+1])
        elif i==list_len-1:
            empty_list.append(inp_list[i-1])
        else:
            empty_list.append(inp_list[i-1])
            empty_list.append(inp_list[i+1])
result_string=""
for i in inp_list:
    if i not in empty_list:
        result_string=result_string+i
print(result_string)
