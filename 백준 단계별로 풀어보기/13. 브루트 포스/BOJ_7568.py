n = int(input())
Dungchi = [list(map(int, input().split())) for _ in range(n)]
a = [1] * n  # 등수 리스트(덩치 큰 사람만큼 카운트)
for i in range(n - 1):
    for j in range(i + 1, n):
        if Dungchi[i][0] > Dungchi[j][0] and Dungchi[i][1] > Dungchi[j][1]:
            a[j] += 1
        elif Dungchi[i][0] < Dungchi[j][0] and Dungchi[i][1] < Dungchi[j][1]:
            a[i] += 1
print(" ".join(map(str, a)))
