# import sys 
from collections import deque

# sys.stdin = open("input.txt", "r")

# input = sys.stdin.read
# data = input().split()
# n = int(data[0])

n = int(input())

# 1단계: 인접 리스트 만들기 (양방향 간선 연결)
graph = [[] for _ in range(n + 1)]
idx = 1
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    idx += 2

# 부모를 저장할 배열 (0이면 아직 방문 안 한 상태)
parent = [0] * (n + 1)

# 2단계: 1번 노드(루트)부터 탐색 시작
queue = deque([1])
parent[1] = 1 # 루트 방문 처리

# 3단계: BFS 탐색 진행
while queue:
    current = queue.popleft()
    
    for next_node in graph[current]:
        if parent[next_node] == 0: # 아직 방문하지 않은 연결 노드라면
            parent[next_node] = current # 방금 출발한 노드(current)가 부모가 됨!
            queue.append(next_node)

# 정답 출력 (2번 노드부터)
for i in range(2, n + 1):
    print(parent[i])