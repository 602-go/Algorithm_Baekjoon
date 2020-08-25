A = input()
B = input()

def multiple(a, b):
    an_3 = int(a) * int(b[2])
    print(an_3)
    an_4 = int(a) * int(b[1])
    print(an_4)
    an_5 = int(a) * int(b[0])
    print(an_5)
    print(an_3+an_4*10+an_5*100)

multiple(A, B)
