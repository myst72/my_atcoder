N = int(input())
A = list(map(int, input().split()))
A_index = {i: [] for i in range(1, N+1)}

for i in range(3*N):
    a = A[i]
    A_index[a].append(i+1)

B = {}
for i in range(1, N+1):
    B[A_index[i][1]] = i
B = sorted(B.items())
ans = [value for key, value in B]
print(*ans)

