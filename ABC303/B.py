from collections import defaultdict
friend = defaultdict(set)
N, M = map(int,input().split())

for _ in range(M):
    a = list(map(int,input().split()))
    for i in range(N):
        ai = a[i]
        if i == 0:
            air = a[i+1]
            friend[ai].add(air)
            ail = ai
        elif i == N-1:
            friend[ai].add(ail)
        else:
            friend[ai].add(ail)
            friend[ail].add(ai)
            ail = ai

            air = a[i+1]
            friend[ai].add(air)
            friend[air].add(ai)

ans = 0
for i in range(N):
    f = friend[i+1]
    ans += N-1-len(f)
print(ans//2)
 