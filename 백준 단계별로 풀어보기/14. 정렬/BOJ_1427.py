nums = list(map(int, list(input()))) #각 문자를 숫자로 반환한 것을 원소로 하는 리스트
nums = sorted(nums, reverse=True) #내림차순정렬
print("".join(map(str,nums))) #우아한 출력 #join과 map 활용