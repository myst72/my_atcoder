X = input()

data = []
for num in range(10):
    #4桁同じ数字
    s1 = str(num)*4
    data.append(s1)

    #連続する数字
    s2 = ""
    for j in range(num, num+4):
        if 10 <= j:
            j = j-10
        s2 += str(j)
    data.append(s2)

if X in data:
    print("Weak")
else:
    print("Strong")