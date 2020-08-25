def hansu(x):
    if x < 100:
        print(x)
    else:
        total = 99
        for i in range(100, x + 1):
            if int(str(i)[1]) - int(str(i)[0]) == int(str(i)[2]) - int(str(i)[1]):
                total += 1
        print(total)


n = int(input())
hansu(n)