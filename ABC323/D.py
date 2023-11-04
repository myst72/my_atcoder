N = int(input())
S = []
C = []
for i in range(N):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

slimes = sorted(zip(S, C), reverse=False)
print(slimes)


i = 0
while True:
    if len(S) == 0:
        print(sum(S))
        break
    else:
        size, slime_count = S[i], C[i]
        print(size, slime_count)
        new_slime_count = slime_count//2
        if new_slime_count == 0:#合体不可
            ans += slime_count
        else:#合体可
            ans = slime_count%2#余り
            new_slime_size = size*2
            if new_slime_size in S:
                C[S.index(new_slime_size)] += new_slime_count
            else:
                C[new_slime_size] = new_slime_count





for size, slime_count in SC.items():
    print(size, slime_count)
    new_slime_count = slime_count//2
    if new_slime_count == 0:#合体不可
        ans += slime_count
    else:#合体可
        ans = slime_count%2#余り
        new_slime_size = size*2
        if new_slime_size in SC.keys():
            SC[new_slime_size] += new_slime_count
        else:
            SC[new_slime_size] = new_slime_count
print(ans)

