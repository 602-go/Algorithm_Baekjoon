# 1. 버블정렬

def BubbleSort(x):
    for j in reversed(range(1, len(x))):
        for i in range(j):
            if x[i] > x[i + 1]:  # 양옆비교하면서 최댓값 뒤로 빼내기 #총 (len(x) -1)번 반복
                x[i], x[i + 1] = x[i + 1], x[i]
    return x


n = int(input())
nums = [int(input()) for _ in range(n)]
for i in BubbleSort(nums):
    print(i)


# 2. 선택정렬
def SelectionSort(x):
    for i in reversed(range(1,len(x))): #리스트에서 최댓값 찾아서 맨 뒤로 빼주기 #총 (len(x)-1)번 반복
        x[i], x[x.index(max(x[0:i+1]))] = max(x[0:i+1]), x[i]
    return x

n = int(input())
nums = [int(input()) for _ in range(n)]
for i in SelectionSort(nums):
    print(i)


# 3. 삽입정렬
def InsertSort(x):
    for i in range(1, len(x)) :
        while (i>0) & (x[i] < x[i-1]) :
            x[i], x[i-1] = x[i-1], x[i]
            i -= 1
    return x

n = int(input())
nums = [int(input()) for _ in range(n)]
for i in InsertSort(nums):
    print(i)