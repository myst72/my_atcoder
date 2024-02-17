N = int(input())
A = list(map(int, input().split()))
A.sort()

Amax = A[-1]
Amax_count = A.count(Amax)
print(A[N-Amax_count-1])