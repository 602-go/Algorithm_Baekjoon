N = int(input())
n = N
cycle = 0
while True:
    if N < 10:
        N = N * 10 + N
        cycle += 1
    else:
        new = int(str(N)[0]) + int(str(N)[1])
        if len(str(new)) == 1:
            N = int(str(N)[1]) * 10 + new
            cycle += 1
        else:
            N = int(str(N)[1]) * 10 + int(str(new)[1])
            cycle += 1

    if N == n:
        print(cycle)
        break