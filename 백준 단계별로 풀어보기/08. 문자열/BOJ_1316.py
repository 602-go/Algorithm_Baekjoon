# sol_1
n = int(input())
total = 0
for _ in range(n):
    x = input()
    words = []
    word = ''
    for i in x:
        if i not in words:
            words.append(i)
            word += i
        else:
            if i == words[-1]:
                word += i
            else:
                continue
    if word == x:
        total += 1
print(total)

# sol_2
n = int(input())
for _ in range(n):
    x = input()
    a = 0
    for i in range(len(x) - 1):
        if x[i] != x[i + 1]:  # 2개씩 체크해서 다른경우
            for j in range(i):  # 앞 알파벳 중 겹치는게 있는지 체크
                if x[j] == x[i + 1]:
                    a = 1  # 있으면 a에 1 부여
    if a == 1:
        n += -1
print(n)
