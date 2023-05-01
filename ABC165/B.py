import math

X = int(input())
money = 100
year = 0

while True:
    if X <= money:
        print(year)
        break
    else:
        year += 1
        money += money//100

