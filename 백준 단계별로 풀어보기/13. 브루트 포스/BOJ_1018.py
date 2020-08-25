#나머지가 짝수, 홀수인지 여부에 따라
n, m = map(int,input().split())
board = [list(input()) for _ in range(n)]
total = 10e7
for i in range(n-8+1):
    for j in range(m-8+1):
        cw, cb, cw_1, cb_1 = 0,0,0,0
        for k in range(i,i+8):
            for s in range(j,j+8):
                #white
                if k%2 == 0:
                    if s%2 == 0:
                        if board[k][s] != "W":
                            cw += 1
                    else:
                        if board[k][s] != "B":
                            cb += 1
                else:
                    if s%2 == 0:
                        if board[k][s] != "B":
                            cb += 1
                    else:
                        if board[k][s] != "W":
                            cw += 1
                #black
                if k%2 == 0:
                    if s%2 == 0:
                        if board[k][s] != "B":
                            cb_1 += 1
                    else:
                        if board[k][s] != "W":
                            cw_1 += 1
                else:
                    if s%2 == 0:
                        if board[k][s] != "W":
                            cw_1 += 1
                    else:
                        if board[k][s] != "B":
                            cb_1 += 1
        if cw + cb <total:
            total = cw+cb
        if cw_1+cb_1 < total:
            total = cw_1+cb_1


print(total)