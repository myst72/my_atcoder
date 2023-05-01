N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

AB = 0
for a, b in zip(A, B):
    AB += a*b

if AB == 0:
    print("Yes")
else:
    print("No")