#import sys
#sys.stdin = open("input.txt", "r")
# 중복없이 수열 => 사용기록 남기기

N, M = map(int, input().split())
# print(N, M)
# 경로 저장
path = []
used = [0]*(N+1)
# cnt: 카드 뽑은 횟수
def recur(cnt):
  #종료 조건
  if cnt == M :
    print(*path)
    return
  # 1~N개의 선택지 중에서 1장 선택
  for i in range(1, N+1):
    #중복확인 
    # 사용한 숫자라면
    if used[i] ==1:
      # 다음으로
      continue
    # 중복이 아니라면 숫자 추가하고
    path.append(i)
    # 사용기록 남기기
    used[i] = 1
    recur(cnt+1)
    path.pop()
    used[i]=0 # 사용기록 초기화(1,4 4,1은 가능하니께)
    

recur(0)

