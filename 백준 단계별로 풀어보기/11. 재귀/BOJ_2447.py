n = int(input())
star = [["*"]*n for i in range(n)]
n_1 = n  #재귀를 돌면서 n이 계속 다르게 계산되기 때문에 함수 내에서 값을 유지할 수 있도록 다른 변수에 할당해둠
def stars(n,x):
    if n == 1:
        return
    else:
        stars(n//3, x) #이전단계까지 다 채우기
        #예시로 생각하기 #n=9일때 #가로세로로 3번씩 총 9번을 반복하며 3*3의 공백을 채워야한다
        for i in range(n_1//n): #27//9
            for j in range(n_1//n): #가로세로 3번씩 iteration 돌게 하는 i와 j
                #여기부터 3*3 공백채우는 것
                for k in range(n//3): #가로(행)
                    for s in range(n//3): #세로(열)
                        x[n*i+n//3+k][n*j+n//3+s] = " " #3*3 공백을 총 9번 채운다. 한칸 씩 공백으로 change
        return x

#2차원 배열 깔끔하게 출력하는 코드
for i in stars(n,star):
    for j in i:
        print(j,end="")
    print()