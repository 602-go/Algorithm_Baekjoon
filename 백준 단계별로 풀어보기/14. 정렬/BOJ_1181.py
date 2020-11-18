n = int(input())

words = [input() for _ in range(n)]
words = list(set(words)) #중복제거
words.sort() #알파벳순 정렬
words.sort(key= lambda x:len(x)) #문자열 길이 순 정렬

for w in words:
    print(w)