n = int(input())
if n % 2 != 0:
    for i in range(n):
        print("*", " *" * (n // 2), sep='')
        print(" *" * (n // 2))
else:
    for i in range(n):
        print("*", " *" * (n // 2 - 1), sep='')
        print(" *" * (n // 2))
