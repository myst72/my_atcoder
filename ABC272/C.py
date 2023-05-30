N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

candidate = [-1]

for i in range(N-1):
    a = A[i]
    for j in range(i+1, N):
        b = A[j]
        s = a+b
        if s%2 == 0:
            candidate.append(s)
            break
print(max(candidate))
