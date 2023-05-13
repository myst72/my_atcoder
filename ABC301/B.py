N = int(input())
A = list(map(int, input().split()))
B = [A[0]]

for i in range(1,N):
    a = A[i]
    b = B[-1]

    if abs(a-b)==1:
        B.append(a)
    else:
        if b<a:
            for c in range(b+1, a+1):
                B.append(c)
        else:
            for c in range(b-1, a-1, -1):
                B.append(c)
print(*B)


