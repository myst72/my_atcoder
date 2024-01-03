N, M = map(int,input().split())
A = list(map(int,input().split()))

result = [0] * (N + 1)

lastday = A[-1]
p = M - 1

for day in range(N, 0, -1):
    if day == lastday:
        result[day] = 0
        p -= 1
        if p >= 0:
            lastday = A[p]
    else:
        result[day] = result[day + 1] + 1

for i in range(1, N + 1):
    print(result[i])
