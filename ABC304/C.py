import math
from collections import deque

def is_infected(N, D, people):
    infected = [False] * N
    infected[0] = True 

    queue = deque([0])
    while queue:
        person = queue.popleft()
        x1, y1 = people[person]

        for i in range(N):
            if not infected[i]:
                x2, y2 = people[i]
                distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if distance <= D:
                    infected[i] = True
                    queue.append(i)

    return infected

N, D = map(int,input().split())
people = list(list(map(int, input().split())) for _ in range(N))
results = is_infected(N, D, people)
for ans in results:
    if ans:
        print("Yes")
    else:
        print("No")