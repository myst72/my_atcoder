N, M = map(int, input().split())
A = list(map(int, input().split()))

votes = [0] * N
max_votes = 0
winner = 1

for i in range(M):
    vote = A[i]
    votes[vote - 1] += 1  # 得票数を更新

    # 現在の得票数の最大値と当選者を更新
    if votes[vote - 1] > max_votes or (votes[vote - 1] == max_votes and vote < winner):
        max_votes = votes[vote - 1]
        winner = vote

    print(winner)
