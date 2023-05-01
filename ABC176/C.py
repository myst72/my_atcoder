N = int(input())
A = list(map(int, input().split()))
ans, m = 0, A[0]

for a in A:
    if a <= m:
        ans += m-a
    else:
        m = a
print(ans)

