# def check(string):
#     len_string = len(string)
#     if len_string%2==0:
#         left_string = string[:len_string//2]
#         right_string = string[:len_string//2-1:-1]
#     else:
#         left_string = string[:len_string//2]
#         right_string = string[:len_string//2:-1]
#     return left_string == right_string

# S = input()
# len_S = len(S)
# ans_list = [1]

# for i in range(len_S):
#     s = S[i]
#     for j in range(len_S-1, i, -1):
#         t = S[j]
#         if s == t:
#             string = S[i:j+1]
#             if check(string):
#                 ans_list.append(len(string))
#             break
# print(max(ans_list))
def F(string):
    max_length = 0
    len_string = len(string)
    
    for i in range(len_string):
        for j in range(i+1, len_string+1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
    
    return max_length

S = input()
ans = F(S)
print(ans)

    
            


