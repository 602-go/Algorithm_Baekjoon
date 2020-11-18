import sys
counts = [0]*(10001) #인풋 제한 10000이하
for i in range(int(input())):
    n = int(sys.stdin.readline())
    counts[n] += 1
for j in range(1,len(counts)):
    if counts[j] != 0:
        for _ in range(counts[j]):
            print(j)