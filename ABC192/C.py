N, K = map(int, input().split())

def g(x):
    str_x = str(x)
    S = []
    for s in str_x:
        S.append(int(s))
    S.sort()
    g1 = ""
    g2 = ""
    for s in S:
        str_s = str(s)
        g1 = g1 + str_s
        g2 = str_s + g2
    g1 = int(g1)
    g2 = int(g2)
    return g1, g2

def f(x):
    g1, g2 = g(x)
    return g2-g1

A = N
for i in range(1, K+1):
    A = f(A)
print(A)