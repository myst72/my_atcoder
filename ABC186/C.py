def check(num,num8):
    if "7" in str(num) or "7" in str(num8):
        return False
    else:
        return True

N = int(input())

ans = 0
for num in range(1, N+1):
    num8 = oct(num)
    if check(num,num8):
        ans += 1
    else:
        pass

print(ans)


