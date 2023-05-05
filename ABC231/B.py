import collections

N = int(input())
S = list(input() for _ in range(N))

S_count = collections.Counter(S)
print(S_count.most_common()[0][0])