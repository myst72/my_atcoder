A = list(map(int, input().split()))
A1 = [i for i, x in enumerate(A) if x == 1]
ans = 0
for a in A1:
    if a==0:
        ans += 1
    else:
        ans += 2**a
print(ans)
