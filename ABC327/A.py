N = int(input())
S = input()

ans = "No"
for i in range(N-1):
    s = S[i]
    s1 = S[i+1]
    if s == 'a' and s1 == 'b' or s == 'b' and s1 == 'a':
        ans = "Yes"
        break
print(ans)