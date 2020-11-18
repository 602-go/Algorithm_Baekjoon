def fibonacci(n):
    zero = [1, 0] #0과 1일 때 count
    one = [0, 1] #0과 1일 때 count
    if n<=1:
        return zero, one #n이 0 또는 1일 때는 초기 리스트 그대로 반환
    else:
        for i in range(2, n+1): #zero와 one 리스트 2번째 값부터 n번째 값까지 채우기
            zero.append(zero[i-2]+zero[i-1])
            one.append(one[i-2]+one[i-1])
        return zero, one

t = int(input())
for _ in range(t):
    n = int(input())
    zero, one = fibonacci(n)
    print(zero[n], one[n])