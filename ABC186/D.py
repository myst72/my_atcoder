#∣5−1∣+∣5−2∣+∣1−2∣ = (5-1)+(5-2)+(2-1) = (5+5+2)-(2+1+1) = (5*2-5*0)+(2*1-2*1)+(1*0-1*2)

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 0
for i in range(N):
    a = A[i]
    ans += a*(N-i-1)-a*i
print(ans)
    

