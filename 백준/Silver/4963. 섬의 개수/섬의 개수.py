# 백준 4963번 문제
# 2차원배열(지도) 주어짐 => graph or map
#정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형
# => 델타 배열(+대각선까지 8방향), bfs
# 1: 땅, 2: 바다, w: 너비(가로) h:높이(세로)
# 최종 결과물: 각 테케의 섬의 갯수 출력
#import sys
#sys.stdin = open("input.txt", "r")
from collections import deque

# 입력 받기
while True:

    # 입력받기
    w, h = map(int, input().split())
    # print(w, h)
    # 마지막 입력줄에는 0 0이 주어짐 => 종료 신호
    if w == 0 and h == 0:
        break
    # mapp 데이터 받기
    mapp = [list(map(int, input().split())) for _ in range(h)]
    # print(mapp)  
    #    

    # 방문 처리 리스트 생성
    visited = [[0]* w for _ in range(h)]
    # 상하좌우 + 대각선 델타 배열 생성
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, -1, 1, 1]
    

    # 섬 넓이 탐색기 설정
    def bfs(start_x, start_y):
        # 큐 지정 및 시작점 지정
        queue = deque([(start_x, start_y)])
        # 시작점 방문처리
        visited[start_x][start_y] = 1
        # queue 빌때까지 반복
        while queue:
            # 큐에 가장 앞에 있는 값 꺼내서 현재좌표로 삼기
            x, y = queue.popleft()
            # 상하좌우 + 대각선 탐색
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                #유효한 범위인지 확인
                if 0<= nx < h and 0<= ny <w:
                    if visited[nx][ny] == 0 and mapp[nx][ny]==1:
                        # 유효한 범위라면 방문기록 및 큐 저장
                        visited[nx][ny] = 1
                        queue.append((nx, ny)) 
                
    cnt = 0
    # 시작점 (1인 지점) 찾기
    # 좌표 접근
    for i in range(h):
        for j in range(w):
            if mapp[i][j] == 1 and visited[i][j] == 0:
                #유효한 조건이라면 탐색기 호출
                bfs(i, j) # 현재 좌표 넘겨주기
                # 한 1 덩어리의 탐색이 끝나면 갯수에 +1 추가
                cnt +=1   

    print(cnt)                 







