#import sys
#sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
li = list(map(int, input().split()))

sort_li = sorted(li)
# print(sort_li)
# 오름차순 수열
# 오름차순 출력
# 중복 불가
path = []
used = [0] *(N+1)

def recur(cnt, start):
  if cnt == M:
    print(*path)
    return
  
  for i in range(start, N):
    if used[i] == 1:
      continue
    path.append(sort_li[i])
    used[i] = 1
    recur(cnt+1, i+1)
    path.pop()
    used[i]= 0

recur(0,0)
