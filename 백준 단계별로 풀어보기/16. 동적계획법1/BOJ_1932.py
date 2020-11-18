n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)] #삼각형 2차원 배열 생성
for i in range(1,n): #1층부터 리스트 요소별로 그 전단계까지의 최댓값 더해나가기
    triangle[i][0] += triangle[i-1][0] #맨 왼쪽은 왼쪽끼리 더해지고
    triangle[i][-1] += triangle[i-1][-1] #맨 오른쪽은 오른쪽끼리 더해질 수 밖에 없음
    for j in range(1,len(triangle[i])-1): #나머지 가운데 친구들은 전단계에서 최대값 찾아와서 더하기
        triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

print(max(triangle[n-1]))