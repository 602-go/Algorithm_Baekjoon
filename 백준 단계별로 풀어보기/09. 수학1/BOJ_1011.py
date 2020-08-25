t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    dist = y-x
    if dist == 1:
        print(1)
    else:
        a = 1
        move = 0
        while True:
            dist = dist - a*2
            move += 2
            if dist > 2*(a+1):
                a += 1
            elif dist == 0:
                break
            elif dist <= 2*(a+1) and dist > a+1:
                move += 2
                break
            else:
                move += 1
                break
        print(move)