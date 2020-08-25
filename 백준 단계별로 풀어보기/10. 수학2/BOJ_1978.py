def find(x):
    total = [i for i in range(2,1001)]
    for i in range(2,1001):
        for j in total:
            if j//i != 1 and j%i == 0:
                total.remove(j)
    ans = 0
    for a in x:
        if a in total:
            ans += 1
    print(ans)


n = int(input())
nums = list(map(int, input().split()))
find(nums)