numbers = [int(input()) for _ in range(10)]

#나머지를 담을 빈 리스트
arr = []
#나머지 계산해서 리스트에 담기
for num in numbers:
    result = num % 42
    arr.append(result)
    
arr_set = set(arr)

print(len(arr_set))