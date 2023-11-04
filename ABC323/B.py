N = int(input())

results = {}
for player in range(N):
    s = input()
    win_counts = s.count("o")
    results[player+1] = win_counts

results2 = sorted(results.items(), key=lambda x:x[1], reverse=True)
ans = []
for i in range(N):
    ans.append(results2[i][0])
print(*ans)


