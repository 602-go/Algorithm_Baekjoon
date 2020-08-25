a = int(input())
for _ in range(a):
    n, word = input().split()
    new = ''
    for i in word:
        new += i*int(n)
    print(new)