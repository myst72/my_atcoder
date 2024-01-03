N, M = map(int, input().split())
C = list(input().split())#皿の色
D = list(input().split())#色
P = list(map(int, input().split()))#値段
P0 = P[0]
P1 = P[1:]
dish = {}
for d, p in zip(D, P1):
    dish[d] = p
    
ans = 0   
for c in C:
    if c in D:
        ans += dish[c]
    else:
        ans += P0
print(ans)