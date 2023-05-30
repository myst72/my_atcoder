import numpy as np

H, W = map(int, input().split())
A = list(list(map(int, input().split())) for _  in range(H))
npA = np.array(A)
m = np.min(npA)
print(sum(sum(npA-m)))





