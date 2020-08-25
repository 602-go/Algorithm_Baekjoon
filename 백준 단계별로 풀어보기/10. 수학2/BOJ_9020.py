# 1. 소수리스트 생성
prime = [i for i in range(2, 10001)]
for i in range(4, len(prime)):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            prime.remove(i)
            break
# 2. 절반부터 소수의 합 찾기
t = int(input())
for _ in range(t):
    n = int(input())
    p = n // 2
    while True:
        if n // 2 in prime:
            print(n // 2, n // 2)
            break
        else:
            p += -1
            if p in prime:
                if n - p in prime:
                    print(p, n - p)
                    break
