total = 1
for _ in range(3):
    total *= int(input())
n = [0]*10
for i in range(len(str(total))):
    n[int(str(total)[i])] += 1
for j in n:
    print(j)