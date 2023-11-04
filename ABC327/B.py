import math
B = int(input())
max_num = int(math.sqrt(B))

A = -1
for a in range(1, max_num+1):
    a2 = a**a
    if a2 == B:
        A = a
    elif a2 > B:
        break
print(A)








