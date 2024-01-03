N = int(input())
S = input()

ans = S.find('ABC')
if ans != -1:
    ans += 1
print(ans)