import re

N = int(input())
S = input()
SC = S.count('o')

ans = -1
pattern = r"o+"
matches = re.findall(pattern, S)
matches = sorted(matches, reverse=True)

for m in matches:
    if "-"+m in S or m+'-' in S:
        ans = len(m)
        break
print(ans)




