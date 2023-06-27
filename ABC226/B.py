N = int(input())
A = []
for _ in range(N):
    a = list(map(int, input().split()))
    a0 = a[0]
    a = a[1:]
    A.append(a)

A_set = set(map(tuple, A))
print(len(A_set))
    