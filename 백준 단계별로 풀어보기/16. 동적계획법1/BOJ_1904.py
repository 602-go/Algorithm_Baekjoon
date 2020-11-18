#처음 수열을 구할 때부터 15746으로 나눈 나머지를 계산
n = int(input())
tiles = [0]*1000001
tiles[1], tiles[2] = 1, 2
for i in range(3,n+1): #n+1이 3보다 작거나 같으면 에러가 뜨는게 아니라 실행안되고 넘어간다.
    tiles[i] = (tiles[i-2] + tiles[i-1])%15746
print(tiles[n])