S = input()
S = S[::-1]
S = S.replace('6', 'x').replace('9', '6').replace('x', '9')
print(S)
