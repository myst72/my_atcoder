def check(positions):
    if (0 in positions and 1 in positions and 2 in positions) or (3 in positions and 4 in positions and 5 in positions) or (6 in positions and 7 in positions and 8 in positions):
        return True
    elif (0 in positions and 3 in positions and 6 in positions) or (1 in positions and 4 in positions and 7 in positions) or (2 in positions and 5 in positions and 8 in positions):
        return True
    elif (0 in positions and 4 in positions and 8 in positions) or (2 in positions and 4 in positions and 6 in positions):
        return True
    else:
        return False

A = []
for _ in range(3):
    a1, a2, a3 = map(int,input().split())
    A.append(a1)
    A.append(a2)
    A.append(a3)

N = int(input())
positions = []
for _ in range(N):
    b = int(input())
    if b in A:
        positions.append(A.index(b))

if check(positions):
    print("Yes")
else:
    print("No")

