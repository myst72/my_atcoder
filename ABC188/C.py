N = int(input())
A = list(map(int, input().split()))
A1, A2 = A[:N//2+1], A[N//2+1:]
p1 = max(A1)
p2 = max(A2)
print(A.index(min(p1,p2))+1)
