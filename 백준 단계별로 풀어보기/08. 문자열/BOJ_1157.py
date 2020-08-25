x = input().upper()
new = {}
for i in set(x):
    new[i] = x.count(i)
if list(new.values()).count(max(new.values())) == 1:
    for i, j in new.items():
        if j == max(new.values()):
            print(i)
else:
    print("?")