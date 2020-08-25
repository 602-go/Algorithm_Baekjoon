n = int(input())
for i in range(n):
    a = input()
    b = [0]*len(a)
    for j in range(len(a)):
        if a[j] == "O":
            b[j] += b[j-1]+1 #직전이 o라면 직전값에 +1을 해주면 된다.
    print(sum(b))