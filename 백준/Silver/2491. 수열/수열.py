#import sys
#sys.stdin = open("input.txt", "r")

N = int(input())
numbers = list(map(int, input().split()))
count = 1
max_len = 1
for i in range(1, N):
    # 만약 i-1번째가 i번째보다 작거나 같으면
    if numbers[i-1] <= numbers[i]:
        # 카운트 +1
        count += 1
    #아니면 카운트 리셋    
    else: 
        count = 1
         
    max_len = max(max_len, count)   

count = 1
for i in range(1, N):
    if numbers[i-1] >= numbers[i]:
        count += 1
    else:
        count = 1

    max_len = max(max_len, count)

print(max_len)
