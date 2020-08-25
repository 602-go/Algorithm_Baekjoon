word = input()
alphabet = list(map(chr,range(97,123)))
ans = [-1]*len(alphabet)
for i in range(len(word)):
    if ans[alphabet.index(word[i])] == -1:
        ans[alphabet.index(word[i])] = i
for j in ans:
    print(j, end= " ")