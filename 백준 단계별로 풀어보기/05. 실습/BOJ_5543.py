h = [int(input()) for i in range(3)]
d = [int(input()) for i in range(2)]

price = 10 ** 10
for i in h:
    for j in d:
        p = i + j - 50
        if p < price:
            price = p
print(price)
