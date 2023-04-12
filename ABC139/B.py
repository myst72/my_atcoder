#最初に1個あるので、B-1口拡張希望
#1個の電源タップでA-1口増える

A, B = map(int, input().split())
x = (B-1) / (A - 1)
y = (B-1) % (A - 1)

if y == 0:
    print(int(x))
else:
    print(int(x)+1)