n = int(input())
pp = [input().split() for _ in range(n)]
pp.sort(key = lambda x: int(x[0]))
for p in pp:
    print(p[0], p[1])