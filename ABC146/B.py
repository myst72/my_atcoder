N = int(input())
S = input()
ans = ""

for s in S:
    new_s = ord(s) + N
    if 91 <= new_s:
        new_s = new_s-26
    ans += chr(new_s)
print(ans)