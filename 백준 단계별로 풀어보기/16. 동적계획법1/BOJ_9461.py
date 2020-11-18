fibo = [0,1,1,1,2,2] + [0]*95
t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(5,n+1):
        fibo[i] = fibo[i-1] + fibo[i-5]
    print(fibo[n])