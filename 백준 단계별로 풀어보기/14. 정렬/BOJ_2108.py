import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(n)]
nums.sort()
# 1. 산술평균
print(round(sum(nums)/n)) #round(n,r) : n의 소수점 아래 r번째에서 반올림
# 2. 중앙값
print(nums[n//2])
# 3. 최빈값 #Counter 함수 활용
c = Counter(nums).most_common(2) #정렬된 nums에서 최빈값 순 튜플형태로 반환
if n == 1: #런타임에러 원인 #예외처리
    #입력값이 1개만 들어오는 경우 최빈값은 인풋값 그대로 반환
    print(nums[0])
else:
    if c[0][1] == c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])
# 4. 범위
print(max(nums)-min(nums))