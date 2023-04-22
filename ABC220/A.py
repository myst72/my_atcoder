A, B, C = map(int,input().split())
ans = -1
for x in range(A, B+1):
    if x % C == 0:
        ans = x
        break
print(ans)
