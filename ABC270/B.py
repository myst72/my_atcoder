X, Y, Z = map(int,input().split())

#ゴールに真っ直ぐ向かう
if (0 < X and (X < Y or Y < 0)) or (X < 0 and (Y < X or 0 < Y)):
    print(abs(X))
else:
    #ゴールの途中にハンマーがある
    if (0 < X and (0 < Z and Z < Y)) or (X < 0 and (Z < 0 and Y < Z)):
        print(abs(X))
    
    #ゴールと反対方向にハンマーがある
    elif (0 < X and Z < 0) or (X < 0 and 0 < Z):
            print(abs(Z)*2 + abs(X))#ハンマーの往復+ゴール

    #ハンマーの前に壁がある
    else:
         print(-1)

