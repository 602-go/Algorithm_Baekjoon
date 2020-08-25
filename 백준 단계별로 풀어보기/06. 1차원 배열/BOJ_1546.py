n = int(input())
scores = list(map(int, input().split()))
avg = 0
for s in scores:
    avg += s/max(scores)*100
print(avg/n)