n = int(input())
dp = [0]+[1]*9 #2차원배열이 아닌 1차원 리스트 #이유는 밑에
if n == 1:
    print(sum(dp))
else:
    for i in range(2,n+1):
        origin = dp.copy() #이전단계 dp는 origin에 복사해두고
        dp[0] = origin[1] #origin을 활용하여 dp를 재정의하면서 업데이트
        for j in range(1,9):
            dp[j] = (origin[j-1]+origin[j+1])
        dp[9] = origin[8]
    print(sum(dp)%1000000000)