n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times = sorted(times, key=lambda x: (x[1],x[0]))
### 이문제에서는 정렬이 중요!! #끝나는 시간 기준으로 정렬 #이후 시작 시간으로 정렬
total = 1
e = times[0][1]
for t in range(1,n):
    if times[t][0] >= e:
        total += 1
        e = times[t][1]
print(total)