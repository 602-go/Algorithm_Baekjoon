def self_number():
    num = [i for i in range(1,10001)]
    for i in range(1, 10001):
        p = i
        for j in range(len(str(i))):
            p += int(str(i)[j])
        try:
            num.remove(p)
        except:
            continue
    for n in num:
        print(n)

self_number()