#1. 파이썬 내장함수 sorted
# 파이썬의 기본 정렬 함수가 O(nlog(n))으로 잘 구성되어 있음
n = int(input())
nums = [int(input()) for _ in range(n)]
for i in sorted(nums):
    print(i)


# 2. 병합 정렬(Merge Sort)
def MergeSort(x):
    if len(x) == 1:
        return x
    else:
        n = len(x) // 2
        left = MergeSort(x[:n])
        right = MergeSort(x[n:])  # 1개가 될 때까지 분할
        i, j = 0, 0
        new = []  # 새로운 정렬 들어갈 리스트 선언
        while True:  # left, right 하나씩 비교해주면서 new에 작은 순대로 넣기
            if left[i] <= right[j]:
                new.append(left[i])
                i += 1
            else:
                new.append(right[j])
                j += 1
            if i == len(left) or j == len(right):
                break
        if i == len(left):  # 종료된 이후에 남은 친구들 new에 넣어주기
            new = new + right[j:len(right)]
        else:
            new = new + left[i:len(left)]
        return new


nums = [int(input()) for _ in range(int(input()))]
print("\n".join(map(str, MergeSort(nums))))


