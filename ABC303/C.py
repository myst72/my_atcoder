from collections import defaultdict

def move(s, now_x, now_y):
    if s == "R":
        now_x += 1
    elif s == "L":
        now_x -= 1
    elif s == "U":
        now_y += 1
    else:
        now_y -= 1
    return now_x, now_y

N, M, H, K = map(int, input().split())
S = input()
items = defaultdict(list)

for _ in range(M):
    x, y = map(int,input().split())
    items[x].append(y)

#移動
now_x, now_y = 0, 0
ans = "Yes"
for s in S:
    if H == 0:
        ans = "No"
        break
    else:
        H -= 1
        now_x, now_y = move(s, now_x, now_y)
        if H<K:
            if now_y in items[now_x]:
                H = K
                items[now_x].remove(now_y)
print(ans)