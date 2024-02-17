def F(month, day): #ゾロ目かどうか判定する関数
    string = str(month) + str(day)
    if len(set(string)) == 1:
        return True
    return False


N = int(input())
D = list(map(int, input().split()))
ans = 0 

for i in range(N):
    month = i + 1
    max_day = D[i]
    for day in range(1, max_day+1):
        if F(month, day):
            ans += 1
print(ans)
