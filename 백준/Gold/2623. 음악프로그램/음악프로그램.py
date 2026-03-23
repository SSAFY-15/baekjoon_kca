import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque
# 위상정렬
# 그래프의 순서를 조건으로


def Topological_sort():
    singer_list = []
    queue = deque()

    # 진입 차수가 0인 노드 queue에 입력 => 출발점
    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)
            
    # queue가 빌 때까지 반복
    while queue:                            
        node = queue.popleft()  
        # 출연 순서 리스트에 현재 노드 저장                
        singer_list.append(node)      

        # 현재 노드에서 갈 수 있는 노드 탐색
        for next_singer in graph[node]: 
             # 다음 노드의 진입 차수 1 감소 (현재 노드와 연결된 간선을 제거하는 역할)        
            degree[next_singer] -= 1    
            # 다음 노드의 진입 차수가 0인 경우
            if degree[next_singer] == 0:   
                # queue에 다음 노드 입력
                queue.append(next_singer) 
                            
    # 모든 가수의 순서를 확정하지 못한 경우 0 출력
    if len(singer_list) != N:               
        print(0)
     # 모든 가수의 순서를 확정한 경우 순서대로 가수의 번호 출력    
    else:                                  
        for singer in singer_list:
            print(singer)

    
# 그래프 그리기
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

# 각 노드의 진입 차수 저장
degree = [0] * (N+1)                

for _ in range(M):
    sequence = list(map(int, input().split()))     # 입력 형태: [가수의 수, 1번 순서 가수, 2번 순서 가수, ...]
    for i in range(1, sequence[0]):
        # 이전 가수의 리스트 공간에 다음 가수의 번호 저장
        graph[sequence[i]].append(sequence[i+1])  
        # 다음 가수의 진입 차수 1 증가      
        degree[sequence[i+1]] += 1                      
        

Topological_sort()         