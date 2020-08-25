# 두 원의 교점 찾기
t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1==x2 and y1==y2:
        if r1 == r2:
            print(-1)
        elif r1>r2 or r1<r2:
            print(0)
    else:
        r = ((x2-x1)**2+(y2-y1)**2)**0.5 #두 원 중심 사이 거리
        if r == r1+r2 or max(r1,r2) == r + min(r1,r2):
            print(1)
        elif r > r2+r1 or max(r1,r2) > r + min(r1,r2):
            print(0)
        else:
            print(2)