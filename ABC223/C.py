N = int(input())
A = []#長さ
B = []#速さ
C = []#時間

for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(a/b)

finish_time = sum(C)/2

ans, time = 0, 0 
for a, b, c in zip(A, B, C):
    if time+c <= finish_time:
        time += c
        ans += a
    else:
        ans += b*(finish_time-time)
        break
print(ans)
