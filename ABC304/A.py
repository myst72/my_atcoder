N = int(input())
names = []

min_index = 0 
min_tall = 10**9
for i in range(N):
    s, a = input().split()
    a = int(a)
    if a <= min_tall:
        min_index = i
        min_tall = a
    names.append(s)

names = names[min_index:]+names[:min_index]
for n in names:
    print(n)
