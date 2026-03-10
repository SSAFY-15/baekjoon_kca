#import sys 
#sys.stdin = open("input.txt", "r")
from collections import deque

#####2. dfs 함수
def dfs(node):
  # 최종 task: 현재 방문한 노드들 출력
  print(node, end=' ')
  #현재 노드들로부터 갈 수 있는 노드들 방문
  for next_node in range(1, N+1):
    #갈 수 없는 노드 pass
    if graph[node][next_node] == 0 :
      continue
    # 이미 방문한 노드 pass
    if visited[next_node] == 1:
      continue
    # 위 둘 다 해당 안돠면 방문처리
    visited[next_node] = 1
    dfs(next_node)


#####3. bfs 함수
def bfs(node):
  # 큐 생성 및 시작점 넣기
  q = deque([(node)])
  # 시작점 방문기록
  visited[node] = 1
  # 큐 빌 때까지 반복
  while q :
    # 가장 먼저 들어온 노드 빼기
    # 현재 뺀 노드가 현재 나의 위치
    now = q.popleft()
    # 현재 위치 출력
    print(now, end=' ')
    # 현재 갈 수 있는 모든 정점 검사(1~N까지)
    for next_node in range(1, N+1):
      if graph[now][next_node] == 0 :
        continue
      if visited[next_node]== 1:
        continue
      # 둘 다 해당 안되면 방문처리
      visited[next_node] =1
      # 다음 노드로 가기위해 큐에 추가
      q.append((next_node))



#####1.입력 받기 및 그래프 생성
# N: 정점 갯수, M: 간선갯수 V:탐색 시작할 정점
N, M, V = map(int, input().split())

# 인접행렬 생성 (정점의 갯수 +1 만큼 => 인덱스 때문에)
graph = [[0]*(N+1) for _ in range(N+1)]
# 방문여부 기록
visited = [0]*(N+1)
# 그래프 연결 초기셋팅

#그래프 간선만큼 for문
for _ in range(M):
  start, end = map(int, input().split())
  # 양방향 설정
  graph[start][end] = 1
  graph[end][start] = 1

# print(graph)  

# 탐색시작(시작점 지정 및 방문처리)
visited[V] = 1
dfs(V)
print()
# visited를 함수 밖에서 생성해서 dfs끝나고 다시 선언(초기화)해야 함
visited = [0]*(N+1)
bfs(V)





  