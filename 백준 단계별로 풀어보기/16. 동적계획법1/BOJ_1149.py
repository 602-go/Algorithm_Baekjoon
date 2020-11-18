n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
#for문으로 각 집의 페인트색마다 앞집까지의 최솟값을 더해나가는 다이나믹 프로그래밍
for i in range(1,n):
    cost[i][0] += min(cost[i-1][1], cost[i-1][2])
    cost[i][1] += min(cost[i-1][0], cost[i-1][2])
    cost[i][2] += min(cost[i-1][0], cost[i-1][1])

print(min(cost[n-1]))