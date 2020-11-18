n = int(input())
time = sorted(list(map(int, input().split())))
total = 0
for i in range(n):
    for j in range(i+1):
        total += time[j]
print(total)