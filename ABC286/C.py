def B_count(S):
    b_count = 0
    S1 = S[:N2]
    S2 = S[:N2-1:-1]
    for i in range(N2):
        if S1[i] != S2[i]:
            b_count+=1
    return b_count

N, A, B = map(int, input().split())
S = input()

N2 = N//2
COST = [B*B_count(S)]

for A_count in range(1, N):
    S = S[1:]+S[0]
    cost = A*A_count+B*B_count(S)
    COST.append(cost)
print(min(COST))


