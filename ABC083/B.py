def num_sum(num):
    str_num = str(num)
    SUM = 0
    for s in str_num:
        SUM += int(s)
    return SUM

def f(N, A, B):
    ans_list = []
    for num in range(1, N+1):
        x = num_sum(num)
        if A <= x <= B:
            ans_list.append(num)
    return ans_list
            
            
N, A, B = map(int,input().split())
ans_list = f(N, A, B)
print(sum(ans_list))