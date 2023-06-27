N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    A_week = A[7*i:7*i+7]
    ans.append(sum(A_week))
print(*ans)