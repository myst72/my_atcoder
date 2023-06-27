def f(S):
    ans = "Yes"
    S1 = S[0]
    for i in range(1, N):
        d = 0
        S2 = S[i]
        for j in range(M):
            if S1[j] != S2[j]:
                d += 1
        if d >= 2:
            ans = "No"
            break
        S1 = S2
    return ans 

N, M = map(int, input().split())
S = [input() for _ in range(N)]
print(S)
S = sorted(S)
print(S)
ans = f(S)
if ans == "Yes":
    print(ans)
else:
    S = sorted(S, reverse = True)
    print(S)
    ans = f(S)
    print(ans)


