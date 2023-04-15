S = input()

lS = len(S)
S00 = S.count("00")#重複せずに現れる回数
ans = lS - S00
print(ans)