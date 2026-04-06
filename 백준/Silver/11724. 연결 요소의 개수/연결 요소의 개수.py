# 요소의 갯수 / 백준 11724번
# 그래프, bfs
import sys
#sys.stdin = open("input.txt", "r")
from collections import deque
input = sys.stdin.readline
# 정점 갯수(N), 간점 갯수(M) 입력받기
N, M = map(int, input().split())
# print(N, M)
# 인접 그래프 만들기
graph = [[] for _ in range(N+1)]

# 그래프 연결
for _ in range(M):
    u, v = map(int, input().split())
    #방향이 없는 그래프 => 양방향 설정
    graph[u].append(v)
    graph[v].append(u)
# 방문 리스트
visited = [0] * (N+1)
# 요소 갯수
count = 0
# bfs 탐색 준비
# 1번부터 N번 노드 까지
for i in range(1, N+1):
    if visited[i] == 0: # 아직 방문 안 한 노드라면 
        count += 1  # 새로운 연결 요소니까 +1
    
        queue = deque([i]) # 앞으로 방문할 노드 담기
        visited[i] = 1 # 방문처리
        
        while queue :# 큐 빌 때까지 반복
            current = queue.popleft()  #큐에 가장 앞에 있는 거 꺼내서 현재 노드로 설정
            # 현재 노드와 연결된 노드들 확인    
            for next_node in graph[current]:

                if visited[next_node] == 0 :# 현재 노드가 아직 방문을 안했다면
                    visited[next_node] = 1 # 방문처리
                    queue.append(next_node) # 다음 검색을 위해 큐에 추가.


print(count)            





