n = int(input())
if n == 1:
    print(1)
else:
    a = 0
    start = 2
    ans = 1
    while True:
        a += 1
        ans += 1
        new = start
        start += 6 * a - 1
        if n >= new and n <= start:
            print(ans)
            break
        start += 1
