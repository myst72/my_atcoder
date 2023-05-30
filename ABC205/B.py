N = int(input())
A = tuple(map(int,input().split()))
sample = tuple(i for i in range(1, N+1))
A = tuple(sorted(A))
if A == sample:
    print("Yes")
else:
    print("No")