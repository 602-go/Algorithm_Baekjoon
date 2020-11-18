## 루프마다 마지막 칸을 기준으로 그 전 칸을 거쳤는지 전전칸을 거쳤는지에 따라 값이 달라짐
# 만약 이전칸에서 바로 올라온 것이라면 이전칸의 dp값을 그대로 가져가면 안되고 이전칸의 전전칸(즉, 세 칸 전)의 dp값을 채택해야함(+이전 칸 점수+현재 칸 점수)
# 만약 전전칸에서 올라온 것이라면 '연속 세 칸 불가능' 조건에 구애받지 않기 때문에 전전칸의 dp값을 그대로 채택하면 된다(+현재 칸 점수)

n = int(input())
stairs = [0]+[int(input()) for _ in range(n)]
dp = [0]*(n+1)
if n==1:
    print(stairs[n])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1]+stairs[2]

    for i in range(3,n+1):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])

    print(dp[n])