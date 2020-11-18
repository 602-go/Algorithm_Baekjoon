n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
total = 0

while True:
    n -= 1
    if k == 0:
        break
    if coins[n] <= k:
        total += k//coins[n]
        k -= (k//coins[n])*coins[n]

print(total)