from collections import Counter
t = int(input())
for _ in range(t):
    c = []
    n = int(input())
    for _ in range(n):
        a,b = input().split()
        c.append(b)
    nums = Counter(c)
    ans = 1
    for n in nums:
        ans *= nums[n]+1
    print(ans - 1)