def F(player, M, S, A):
    """現在の得点と残りの問題を算出する"""
    now_point = player+1
    dpoint_list = []
    for question in range(M):
        if S[question] == "o":
            now_point += A[question]
        else:
            dpoint_list.append(A[question])
    return now_point, sorted(dpoint_list, reverse=True)



def main():
    N, M = map(int, input().split())

    A = list(map(int,input().split()))
    A_dic = {}
    for question in range(M):
        A_dic[question] = A[question]
    
    now_point_list = []
    dpoint_list2 = []
    for player in range(N):
        S = input()
        now_point, dpoint_list = F(player, M, S, A)
        now_point_list.append(now_point)
        dpoint_list2.append(dpoint_list)
    
    max_point = max(now_point_list)
    for player in range(N):
        point = now_point_list[player]
        if point == max_point:
            ans = 0
        else:
            d = max_point-point
            ans = 0
            while True:
                if d<=0:
                    break
                else:
                    ans += 1
                    d -= dpoint_list2[player].pop(0)
        print(ans)

main()