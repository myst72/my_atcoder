N = int(input())
A = list(map(int, input().split()))

current_passengers = 0
min_initial_passengers = 0
for a in A:
    current_passengers += a
    if current_passengers < 0:
        min_initial_passengers += -current_passengers
        current_passengers = 0
        
ans = min_initial_passengers + sum(A)
print(ans)


