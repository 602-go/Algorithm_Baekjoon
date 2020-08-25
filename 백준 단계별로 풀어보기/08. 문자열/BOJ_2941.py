alphabet = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
x = input()

for a in alphabet:
    x = x.replace(a, "*")

print(len(x))