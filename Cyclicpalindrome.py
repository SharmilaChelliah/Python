inp = input()
flag = 0
length  = len(inp)
string_list_temporary = list(inp)
first_character = inp[0]
del string_list_temporary[0]
string_list_temporary.append(first_character)
string_tem = ''.join(string_list_temporary)
if string_tem == string_tem[::-1]:
    print(1)
    flag = 1
string_list_temporary_1 = list(inp)
last_character = inp[len(inp) - 1]
del string_list_temporary_1[len(inp)-1]
string_tem_1 = last_character + ''.join(string_list_temporary_1)
if string_tem_1 == string_tem_1[::-1]:
    print(1)
    flag = 1
if flag == 0:
    print(-1)
