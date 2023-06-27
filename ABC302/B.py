def f(i, j):
    directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for (dx, dy) in directions:
        if i+dx*4<H and j+dy*4<W:
            if S[i+dx*1][j+dy*1] == "n" and S[i+dx*2][j+dy*2] == "u" and S[i+dx*3][j+dy*3] == "k" and S[i+dx*4][j+dy*4] == "e":
                return [[i,j], [i+dx*1, j+dy*1], [i+dx*2, j+dy*2], [i+dx*3, j+dy*3], [i+dx*4, j+dy*4]]
    return False

H, W = map(int, input().split())
snuke_s = []

S = []
for i in range(H):
    si = input()
    for j in range(W):
        sij = si[j]
        if sij == "s":
            snuke_s.append((i,j))
    S.append(si)

for (sx, sy) in snuke_s:
    ans = f(sx, sy)
    if ans != False:
        break

for (ax, ay) in ans:
    print(ax+1, ay+1)











