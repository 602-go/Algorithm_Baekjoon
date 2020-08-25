def triangle(x):
    m = max(x)
    x.remove(m)
    if m ** 2 == x[0] ** 2 + x[1] ** 2:
        print("right")
    else:
        print("wrong")


while True:
    x = list(map(int, input().split()))
    if 0 in x:
        break
    else:
        triangle(x)
