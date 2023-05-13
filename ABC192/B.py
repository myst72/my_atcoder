S = input()
LS = len(S)
ans = "Yes"

for i in range(LS):
    s = S[i]

    #奇数番目
    if i%2 == 0:
        if s.isupper():
            ans = "No"
            break
    else:
        if s.islower():
            ans = "No"
            break
print(ans)
            

