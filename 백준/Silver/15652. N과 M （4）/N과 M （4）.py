#import sys
#sys.stdin = open("input.txt", "r")

# 중복 가능. 
# 비 내림차순

N, M = map(int, input().split())

path = []
used = [0] * (N+1)


def recur(cnt,start):
  if cnt == M:
    print(*path)
    return
  i = 1
  for i in range(start, N+1):
    # if used[i] == 1:
    #   continue
    path.append(i)
    # used[i] = 1
    recur(cnt+1, i)
    path.pop()
    # used[i] = 0

recur(0, 1)    