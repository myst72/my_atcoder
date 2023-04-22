N = int(input())
money = 0

for day in range(N):
    money += day+1
    if N <= money:
        print(day+1)
        break