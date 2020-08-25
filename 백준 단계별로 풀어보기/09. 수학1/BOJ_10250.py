t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    y = n%h
    if y == 0:
        y = h
        x = n//h
    else:
        x = n//h + 1
    if x<10:
        print("{}0{}".format(y,x))
    else:
        print("{}{}".format(y,x))