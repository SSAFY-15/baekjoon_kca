
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# print(numbers)
flg = True
total = 0
max_total = []

# 첫번째 카드 설정
for i in range(N):
  total += numbers[i]
  
  # 두번째 카드 설정
  for j in range(i+1, N):
    total += numbers[j]
   
    # 세번째 카드 설정
    for k in range(j+1, N):
      total += numbers[k]
     
      # 다 돌았는데, total이 M보다 크면 break
      if total > M:
        total -= numbers[k]
        # print(total)
        continue  
        
      # 아니라면 total을 max_total list에 넣기
      else:
        max_total.append(total)    
        total -= numbers[k]
  
    total -=numbers[j]

  total -= numbers[i]  
      
   
print(max(max_total))

