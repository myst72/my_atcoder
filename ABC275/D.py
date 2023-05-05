def f_memoized(k):
    if k in _memo:
        y =  _memo[k]
    else:
        if k==0:
            y = 1
        else:
            y = f_memoized(k//2)+f_memoized(k//3)
        _memo[k] = y
    return y
    
N = int(input())
_memo = {}
y = f_memoized(N)
print(y)