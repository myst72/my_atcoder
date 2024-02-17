def removeABC(S):
    S1 = []
    for s in S:
        if s == 'C' and S1[-2:] == ['A', 'B']:
            S1.pop()
            S1.pop()
        else:
            S1.append(s)
    return ''.join(S1)

S = input()
ans = removeABC(S)
print(ans)

