N = int(input())
S = input()
T = input()

ans = "Yes"
for i in range(N):
    s, t = S[i], T[i]
    if s != t:
        if (s == "1" and t == "l") or (s == "l" and t == "1"):
            pass
        elif (s == "0" and t == "o") or (s == "o" and t == "0"):
            pass
        else:
            ans = "No"
            break
print(ans)

