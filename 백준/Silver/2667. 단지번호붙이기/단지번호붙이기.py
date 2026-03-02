#백준 2667번
#import sys
#sys.stdin = open("input.txt", "r")

from collections import deque

#입력받기
N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
# print(N, graph)

# 방문 리스트
visited = [[0] * N for _ in range(N)]
#상하좌우 좌표 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 

# 단지 탐색기 설정(bfs 함수)
def bfs(start_x, start_y, graph, N):
    #큐 시작점 설정
    queue = deque([(start_x, start_y)])
    # 시작점 방문기록
    visited[start_x][start_y] = 1
    # 넓이 기본값 설정: 1인 곳을 찾아서 bfs를 호출한 것이므로 현재 위치는 1 => 현재 위치도 넓이에 포함
    area_size = 1
    #사방향 탐색 while 문
    # queue가 빌 떄까지
    while queue:
        #일단 queue에서 앞에 있는 값 빼서 현재 좌표로 지정
        x, y = queue.popleft()
        # 4방향(상하좌우) 탐색
        for i in range(4):
            #다음으로 갈 좌표 지정
            nx = x + dx[i]
            ny = y + dy[i]
            # 유효한 범위인지 탐색(graph를 벗어나는지 확인)
            if 0 <= nx < N and 0 <= ny < N:
                # 방문한 곳인지, 값이 1인 곳인지 확인
                if visited[nx][ny] ==0 and graph[nx][ny] == 1:
                    # 유효한 범위라면
                    # 1. 방문처리
                    visited[nx][ny] = 1
                    # 2. 넓이 추가하고
                    area_size +=1
                    # 3. 현좌표를 기준으로 다음을 탐색하기 위해. queue에 저장
                    queue.append((nx, ny))
    # 4방향 탐색으 끝나면 최종 넓이 반환
    return area_size 
# 전체 덩어리 갯수
cnt = 0 
result_list = []
# 메인루프(값이 1인 곳 찾기 찾으면 넓이 탐색기(bfs 함수)호출해서 넓이 측정)  
# 좌표 진입             
for i in range(N):
    for j in range(N):
        # 현재 좌표 값이 1이라면
        if graph[i][j] == 1 and visited[i][j]==0:
            # 넓이 측정기 호출.그리고 결과 값을 result에 저장
            result = bfs(i, j, graph, N)
            result_list.append(result)
            # 한 덩어리의 넓이 측정이 끝나rh  갯수 추가
            cnt +=1
            
# print(result_list)            
sort_list = sorted(result_list) 

print(cnt)
print(*sort_list, sep='\n')   
            





