n = int(input())
counts = 0
nums = 666 #시작은 666부터
while True:
    if counts == n: #count가 n번째까지 진행되면 종료
        break
    if "666" in str(nums): #숫자 1씩 늘리면서 666 포함하면 ans로 저장후 count +1
        ans = nums
        counts += 1
    nums += 1 #숫자 1씩 늘리면서 루프돌기
print(ans)