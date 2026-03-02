# 백준 2178번 미로탐색 문제
# N×M크기의 배열로 표현되는 미로: 2차원 배열(graph)
# 서로 인접한 칸으로만 이동: 델타배열(상하좌우, 대각선은 X)
# 최단거리 : bfs, 거리누적
# 출발:(1,1) 도착(N, M) N=가로 M = 세로

#import sys
#sys.stdin = open("input.txt", "r")

from collections import deque

# 길이 탐색기 
def bfs(start_x, start_y):
    # 큐 생성 및 시작점 지정
    queue = deque([(start_x, start_y)])
    # 시작점 방문 처리
    visited[start_x][start_y] = 1
    lenn = 0
    # queue 빌 때까지 반복
    while queue:
        # 큐에서 가장 앞에 꺼 뺴서 현재지점으로 지정
        x, y = queue.popleft()
        # 현재 위치를 기준으로 4방향 탐색
        for i in range(4):
            nx = x+ dx[i]
            ny = y + dy[i]
            #유효범위 확인
            if 0 <= nx < N and 0 <= ny < M :
                if visited[nx][ny] == 0 and mapp[nx][ny] ==1 :
                    #유효범위라면 방문처리 및 큐에 저장
                    visited[nx][ny] =1
                    # 최단거리는 지나간 칸의 바닥에 출발점으로 부터  몇 걸음 째인지 숫자를 적어야 함. 
                    mapp[nx][ny] = mapp[x][y] +1
                    queue.append((nx, ny))
                    
    # 탐색 끝나면 도착점 바닥에 적힌 숫자 반환(인덱스 때문에 -1)                
    return mapp[N-1][M-1]
                
# 입력받기
N, M = map(int, input().split())
mapp = [list(map(int, input())) for _ in range(N)]
# print(mapp)

# 방문처리 리스트 생성
visited = [[0]* M for _ in range(N)]

#델타 배열
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 시작점
print(bfs(0, 0))




            







