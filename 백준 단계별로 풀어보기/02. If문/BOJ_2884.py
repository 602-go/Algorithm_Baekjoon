H, M = map(int, input().split())
if H == 0:
    if M<45:
        print("23", 60-45+M)
    else:
        print(H, M-45)
else:
    if M<45:
        print(H-1, 60-45+M)
    else:
        print(H, M-45)    