N = int(input())
S = input()

T = S.count("T")
A = S.count("A")
if T<A:
    print("A")
elif T>A:
    print("T")
else:
    if S[-1] == "T":
        print("A")
    else:
        print("T")