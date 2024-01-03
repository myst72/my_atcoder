S = list(map(int, input().split()))
s0 = 0
ans = "Yes"
for s in S:
    if (s0 <= s) and (100<=s<=675) and (s%25==0):
        s0 = s
        pass
    else:
        ans = "No"
        break

print(ans)
