prime = [1]*(123456*2+1) #미리 소수들을 전부 구해놓고 리스트 인덱싱으로 개수구하기
prime[0] = 0
prime[1] = 0
for i in range(4, len(prime)):
    for j in range(2, int(i**0.5)+1):
        if i%j == 0:
            prime[i] = 0
            break
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(prime[n+1:2*n+1]))