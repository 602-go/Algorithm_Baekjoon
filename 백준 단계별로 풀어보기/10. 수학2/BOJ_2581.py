M = int(input())
N = int(input())
nums = [n for n in range(M, N+1)]
if 1 in nums:
    nums.remove(1)
for i in range(2,N):
    for n in nums:
        if n//i != 1 and n%i == 0:
            nums.remove(n)


if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))