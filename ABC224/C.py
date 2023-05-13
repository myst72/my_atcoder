N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ans = 0
#正の面積を持つ三角形:一直線上に並ばない
#(y2-y1)/(x2-x1) != (y3-y1)/(x3-x1)
#(x2-x1)*(y3-y1) != (x3-x1)*(y2-y1)
for i in range(N-2):
    x1, y1 = X[i], Y[i]
    for j  in range(i+1, N-1):
        x2, y2 = X[j], Y[j]
        dx1 = x2-x1
        dy1 = y2-y1
        for k in range(j+1, N):
            x3, y3 = X[k], Y[k]
            dx2 = x3-x1
            dy2 = y3-y1
            if dx1*dy2 != dx2*dy1:
                ans += 1
print(ans)

