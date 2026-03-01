#백준 1926번
from collections import deque
#import sys
#sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# print(n, m)
# print(graph)
# visited 
# 방향벡터 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False]*m for _ in range(n)]
# print(visited)

def bfs(start_x, start_y, graph, n, m):
    # 큐 생성, 시작점 표시
    queue=deque([(start_x, start_y)])
    # 시작점 방문 처리
    visited[start_x][start_y] = True
    area_size = 1

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4방향 탐색
        for i in range(4):
            nx = x +dx[i]
            ny = y+ dy[i]
            # 유효범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    # 유효범위라면 방문처리 후 큐에 삽입
                    visited[nx][ny] = True 
                    queue.append((nx, ny))
                    area_size += 1


    return area_size   

cnt = 0
max_area = 0
for i in range(n) :
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            # bfs(i, j, graph, n, m)
            result = bfs(i, j, graph, n, m)
            if result >= max_area :
                max_area = result
            cnt += 1
                  
 
print(cnt)
print(max_area)
    



