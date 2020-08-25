t = int(input())
for _ in range(t):
    k, n = int(input()), int(input())
    apart = [[0] * n for _ in range(k + 1)]
    for i in range(n):  # 0층부터 채우기
        apart[0][i] = i + 1
    for i in range(1, k + 1):  # 1층부터 k층까지 채우기
        apart[i][0] = 1
        for j in range(1, n):  # 층 별로 호수 순으로 차례로 채우기
            for s in range(j + 1):
                apart[i][j] += apart[i - 1][s]
    print(apart[k][n - 1])
