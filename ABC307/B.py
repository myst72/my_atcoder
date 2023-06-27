def check(a,b):
    s = a+b
    len_s2 = len(s)//2
    if (len(s)%2 == 0) and (s[:len_s2] == s[:len_s2-1:-1]):
        return True
    elif (len(s)%2 != 0) and (s[:len_s2] == s[:len_s2:-1]):
        return True
    else:
        return False
    

N = int(input())
S = [input() for _ in range(N)]
ans = "No"
for i in range(N-1):
    for j in range(i+1, N):
        if check(S[i],S[j]) or check(S[j],S[i]):
            ans = "Yes"
            print(ans)
            exit()
print(ans)
        



