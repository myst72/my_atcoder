import numpy as np

N, T = map(int,input().split())
C = list(map(int,input().split()))
R = list(map(int,input().split()))


def search(T):
    np_C = np.array(C)
    PlayerT = np.where(np_C == T)[0]

    a = 0
    for Player in PlayerT:
        if R[Player] > a:
            a =  R[Player]
            winner = Player+1
    return winner

if T in C:
    winner = search(T)
else:
    winner = search(C[0])
print(winner)
        
