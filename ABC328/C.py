N, Q = map(int, input().split())
S = input()

memo = [0] * (N + 1)
for i in range(1, N):
    if S[i] == S[i - 1]:
        memo[i + 1] = memo[i] + 1
    else:
        memo[i + 1] = memo[i]


for _ in range(Q):
    l, r = map(int, input().split())
    point = memo[r] - memo[l]
    print(point)
    
