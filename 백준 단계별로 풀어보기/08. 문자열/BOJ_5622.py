dial = {2: ["A", "B", "C"], 3: ["D", "E", "F"], 4: ["G", "H", "I"], 5: ["J", "K", "L"], 6: ["M", "N", "O"],
        7: ["P", "Q", "R", "S"], 8: ["T", "U", "V"], 9: ["W", "X", "Y", "Z"]}
x = input()
total = 0
for i in x:
    for n, w in dial.items():
        if i in w:
            total += n + 1
print(total)
