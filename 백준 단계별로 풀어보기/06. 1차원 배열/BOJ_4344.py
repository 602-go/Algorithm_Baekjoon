c = int(input())
for _ in range(c):
    scores = list(map(int, input().split()))
    avg = (sum(scores) - scores[0])/scores[0]
    great = 0
    for i in range(1, scores[0]+1):
        if scores[i] > avg:
            great += 1
    print("%.3f"%(great/scores[0]*100), "%", sep='')