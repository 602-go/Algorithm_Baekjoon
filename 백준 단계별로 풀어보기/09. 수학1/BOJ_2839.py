n = int(input())
case = []
for i in range(n // 5 + 1):
    for j in range(n // 3 + 1):
        if 5 * i + 3 * j == n:
            case.append(i + j)
if len(case) == 0:
    print(-1)
else:
    print(min(case))
