N = int(input())
ST = []
for _ in range(N):
    s, t = input().split()
    ST.append((s, int(t)))

ST.sort(key=lambda x: x[1])
print(ST[-2][0])



    
