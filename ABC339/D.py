from collections import deque

def BFS(N, S, players):
    D = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 上右下左
    if players[0] == players[1]:  # 終了
        return 0

    queue = deque([(players[0], players[1], 0)])
    visited = {(players[0], players[1]): True}

    while queue:
        pos1, pos2, moves = queue.popleft()
        for d in D:
            next_pos1 = (pos1[0] + d[0], pos1[1] + d[1])
            next_pos2 = (pos2[0] + d[0], pos2[1] + d[1])

            if next_pos1[0] < 0 or next_pos1[0] >= N or next_pos1[1] < 0 or next_pos1[1] >= N or S[next_pos1[0]][next_pos1[1]] == '#':
                next_pos1 = pos1
            if next_pos2[0] < 0 or next_pos2[0] >= N or next_pos2[1] < 0 or next_pos2[1] >= N or S[next_pos2[0]][next_pos2[1]] == '#':
                next_pos2 = pos2
            
            if next_pos1 == next_pos2:
                return moves + 1

            if (next_pos1, next_pos2) not in visited:
                visited[(next_pos1, next_pos2)] = True
                queue.append((next_pos1, next_pos2, moves + 1))

    return -1



def main():
    N = int(input())
    S = []
    players = []
    for i in range(N):
        s = input()
        S.append(s)
        for j in range(N):
            if s[j] == "P":
                players.append((i, j))
    ans = BFS(N, S, players)
    print(ans)


if __name__ == '__main__':
    main()

