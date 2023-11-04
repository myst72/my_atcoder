import numpy as np

def check_row(A):
    for row in A:
        if set(row) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            continue
        else:
            return False
    return True

def check_col(A):
    for col in A.T:
        if set(col) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            continue
        else:
            return False
    return True

def check_block(A):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = A[i:i+3, j:j+3]
            if set(block.flatten().tolist()) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                continue
            else:
                return False
    return True

A = np.array(list(list(map(int, input().split())) for _ in range(9)))
if check_row(A) and check_col(A) and check_block(A):
    print("Yes")
else:
    print("No")
