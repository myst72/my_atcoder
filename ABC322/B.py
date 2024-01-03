N, M = map(int,input().split())
S = input()
T = input()

start = T.startswith(S)
end = T.endswith(S)

if start and end:
    print(0)
elif start:
    print(1)
elif end:
    print(2)
else:
    print(3)
