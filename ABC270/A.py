A, B = map(int,input().split())

A2 = format(A, '03b')
B2 = format(B, 'b')

#ビット単位論理和
ans = int(bin(A | B), 2)
print(ans)