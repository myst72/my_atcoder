N, M = map(int, input().split())
A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))

ans = abs(A[0]-B[0])
n = 0
m = 0

while True:
    if n == N or m == M:
        print(ans)
        break

    a = A[n]
    b = B[m]

    d = abs(a-b)
    ans = min(ans, d)

    if a<=b:
        d = b-a
        n += 1
    else:
        d = a-b
        m += 1
    ans = min(ans, d)






