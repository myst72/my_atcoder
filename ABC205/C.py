def f(A, B):
    if A<B:
        return "<"
    elif A == B:
        return "="
    else:
        return ">"

A, B, C = map(int, input().split())

if 0<A*B:#同符号
    ans = f(A, B)

else:#異符号
    if C%2==0:#指数:偶数
        ans = f(abs(A), abs(B))
    else:
        ans = f(A, B)
print(ans)