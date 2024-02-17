H, W, N = map(int, input().split())
gred = [['.' for i in range(W)]for _ in range(H)]

D = [(-1, 0), (0, 1), (1, 0), (0, -1)]#上右下左
x, y, d = 0, 0, 0

for time in range(N):
    x, y= x%H, y%W
    if gred[x][y] == '.':#白いマス
        gred[x][y] = '#'
        d = (d + 1) % 4
        dx, dy = D[d][0], D[d][1]
        x, y = x + dx, y + dy
    else:#黒いマス
        gred[x][y] = '.'
        d = (d - 1) % 4
        dx, dy = D[d][0], D[d][1]
        x, y = x + dx, y + dy

for i in range(H):
    print(''.join(gred[i]))


    




