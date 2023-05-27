N = int(input())
A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 10**10
for i in range(N):
    a = A[i]
    for j in range(N):
        b = B[j]
        if i==j:
            ans = min(ans, a+b)
        else:
            ans = min(ans, max(a,b))
print(ans)