n = int(input())
point = [list(map(int, input().split())) for _ in range(n)]
point = sorted(point)
for p in point:
    print(" ".join(map(str, p)))