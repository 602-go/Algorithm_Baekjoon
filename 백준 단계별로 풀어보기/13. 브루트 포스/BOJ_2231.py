n = int(input())
p = 0
for i in range(n):
    total = i
    for j in range(len(str(i))):
        total += int(str(i)[j])
    if total == n:
        p = 1
        print(i)
        break
if p != 1:
    print(0)