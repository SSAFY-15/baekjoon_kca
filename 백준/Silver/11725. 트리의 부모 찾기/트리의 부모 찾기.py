# 백준 11725번 트리의 부모찾기 문제
# 알고리즘 분류: 그래프 탐색, 트리, bfs

# 입력 받기
import sys
# 덱 설정
from collections import deque

#메모리 최적화 - 한 줄씩 빠르게 읽어오기
input = sys.stdin.readline

## 입력받기 + 그래프 만들기
N = int (input()) # 노드 갯수 입력받기
graph = [[] for _ in range(N+1)] # 인접 그래프 만들기

## 그래프 연결하기 (간선 정보 입력)
for _ in range(N-1):  #트리의 간선 갯수는 노드갯수-1
    u, v = map(int, input().split())
    # 방향이 없음. 양방향 설정
    graph[u].append(v)  # u번 노드의 리스트에 v 추가
    graph[v].append(u)  # v번 노드의 리스트에 u 추가



### bfs 탐색 준비
parent = [0]*(N+1) #  각 노드의 부모 번호를 저장할 배열
                   # 0이면 아직 한 번도 방문하지 않은 노드
queue = deque([1])  # 1번 노드(루트)부터 탐색 시작
parent[1]= 1 # 루트 방문 처리

# parent = [0], [1], [0], [0], [0], [0], [0]

## bfs 탐색 진행
# queue 빌 때까지 반복
while queue:
    current = queue.popleft() # 큐에 가장 먼저 들어온 노드를 하나 꺼내서 current로 지정
                                # current: 현재 머무는 노드
    for next_node in graph[current]: # current 노드와 연결된 인접 노드들 확인
                                     # next_node: current노드와 연결된 인접 노드
        
        if parent[next_node] == 0: # 아직 방문하지 않은 노드라면
            parent[next_node] = current # 방금 출발한 노드(current)가 부모가 됨
            queue.append(next_node) # 큐에 next_node 넣기

# 2번 노드부터 정답 출력 
for i in range(2, N +1):
    print(parent[i])





# if parent[next_node] == 0: 
# => 노드가 왔던 길을 다시 되돌아가지 않도록 방지턱 역할
# 1번노드 -> 6번노드 -> 다시 1번노드 -> 다시 6번노드 이런식으로 무한루프가 생성됨.