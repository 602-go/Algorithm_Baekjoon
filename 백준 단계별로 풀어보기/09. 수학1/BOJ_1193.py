x = int(input())
if x == 1:
    print("1/1")
else:
    start = 2
    b = 1
    while True:
        b += 1
        new = start+b-1
        if x>=start and x<=new:
            if b%2==0:
                ja = 1 + (x-start)
                mo = (b+1) - ja
                print(ja,"/",mo, sep = '')
                break
            else:
                mo = 1 + (x-start)
                ja = (b+1) - mo
                print(ja,"/",mo, sep = '')
                break
        start = new + 1