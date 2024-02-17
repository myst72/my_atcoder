import math

def find_min_abs_difference(D):
    # 初期化: 最小値を大きな値に設定
    min_diff = float('inf')

    # xを0からsqrt(D)まで繰り返し探索
    for x in range(int(math.sqrt(D)) + 1):
        y_squared = D - x**2
        y = math.sqrt(y_squared)

        # yが整数なら、最小値は0
        if y.is_integer():
            return 0

        # yが整数でない場合、差の絶対値を計算し、最小値を更新
        diff = abs(x**2 + y_squared - D)
        min_diff = min(min_diff, diff)

    return min_diff

D = int(input())
print(find_min_abs_difference(D))