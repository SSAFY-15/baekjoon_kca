N, M = map(int, input().split())
path =[]
used = [0]*(N+1)

#cnt: 카드 뽑은 횟수
def recur(cnt, start):
  # 종료조건
  if cnt == M:
    print(*path)
    return
  # N개 중에서 1개 뽑는 반복문
  i = 1
  for i in range(start, N+1):
    # 사용여부 확인
    if used[i] ==1:
      continue
    #사용여부 없으면, 경로에 추가하고
    path.append(i)
    #사용여부 기록
    used[i] = 1
    # 다음 카드 뽑기
    recur(cnt+1, i+1)
    # 다음 턴을 위해서 pop
    path.pop()
    # 사용여부 초기화
    used[i] = 0


recur(0, 1)    