N = int(input())
ST = set()
for _ in range(N):
    s, t = input().split()
    ST.add((s,t))
if len(ST) == N:
    print("No")
else:
    print("Yes")