#import sys
#sys.stdin = open("input.txt", "r")

# 중복불가
# 오름차순으로 출력


N, M = map(int, input().split())

li = list(map(int, input().split()))

# 미리 오름차순으로 정렬
sort_li = sorted(li)
# print(sort_li)

path = []
used = [0] * (N+1)

def recur(cnt):
  if cnt == M :
    print(*path)
    return 
  
  for i in range(N):
    if used[i] == 1:
      continue
    # 사용 X면, path에 추가
    path.append(sort_li[i])
    # 사용기록 
    used[i] = 1
    # 다음 숫자 뽑기
    recur(cnt+1)
    #다음 사용을 위해 pop
    path.pop()
    # 사용기록 초기화
    used[i] = 0

recur(0)
 

