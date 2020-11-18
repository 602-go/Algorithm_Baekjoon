import sys

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
#세상 모든 수는 m으로 나눴을 때 나머지가 0~(m-1)이다
#가능한 m을 오름차순으로 출력
#이렇게 하면 시간초과...
m = 2
while m!=max(nums):
    p=0
    ans = nums[0] % m
    for s in range(1, len(nums)):
        if nums[s] % m != ans:
            p=1
            break
    if p == 0:
        print(m, end=" ")
    m += 1