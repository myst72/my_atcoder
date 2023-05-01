N = int(input())
S = input()

C = 0
for i in range(N):
    s = S[i]
    if s == '|':
        C += 1
    elif s == '*':
        if C == 1:
            ans = "in"
        else:
            ans = "out"
        break
print(ans)