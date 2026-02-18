N = int(input())
heights = [0] * 1001
for _ in range(N):
    L, H = map(int, input().split())     
    heights[L] = H

# print(heights)  
# 최고점의 높이와 인덱스 찾기
max_h = 0
for h in heights:
    if h >= max_h:
        max_h = h
        max_idx = heights.index(max_h) 

left_max = 0
total_sum = 0
# 왼쪽 스캔(0~max-idx까지)
for i in range(max_idx+1):# +1안하면 최고점 안 더함.
    # 만약 i번째 높이가 더 크다면
    if heights[i] > left_max:
        # max값 갱신
        left_max = heights[i]
    # 아니라면 계속 더하기
    total_sum += left_max

right_max = 0 
total_sum2 = 0
#오른쪽 스캔 (1000~ idx_max까지)
for i in range(1000, max_idx, -1):
    # 만약 i번째 높이가 더 크다면
    if heights[i] > right_max:
         # max값 갱신
        right_max = heights[i]
    # 아니라면 계속 더하기
    total_sum2 += right_max  

result = total_sum + total_sum2
print(result)    
