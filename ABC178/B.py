a, b, c, d = map(int,input().split())

x1 = a*c
x2 = b*c
x3 = a*d
x4 = b*d
print(max(x1, x2, x3, x4))
