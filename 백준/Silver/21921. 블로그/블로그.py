# 슬라이싱 윈도우


# N: 전체일수, X: 계산할 기간
N, X = map(int, input().split()) 
arr = list(map(int, input().split()))

# 0일부터 x-1일까지 첫번째 윈도우합 계산 : 기준점
window = sum(arr[:X]) 

# 2일동안 가장 많은 방문자 수
max_window = window
max_day = 1 #최대값이 나타난 횟수

for i in range(N-X):
    window = window - arr[i] + arr[i+X]
    # 최대 window 갱신
    if window > max_window:
        max_window = window
        max_day =1
    # 2. 최대값이 동일하다면, max_day += 1
    elif window == max_window:
        max_day += 1
# 만약 방문자가 없다면
if max_window == 0:
    print('SAD')

else:
    print(max_window)
    print(max_day)

   



