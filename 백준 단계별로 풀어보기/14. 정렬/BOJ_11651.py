#1. 내장함수 sorted
n = int(input())
point = [list(map(int, input().split()))[::-1] for _ in range(n)]
point = sorted(point)
for p in point:
    print(p[1], p[0])

#2. sort와 lambda 활용
n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]
point.sort(key=lambda x: (x[1], x[0]))
for p in point:
    print(p[0], p[1])