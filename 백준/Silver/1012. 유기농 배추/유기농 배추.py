# 백준 1012번 유기농 배추 문제
# 상하좌우=>델타 배열
# 2차원 공간(배추밭) => 그래프 탐색
# "인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다"
# => bfs
# 최종 결과: 필요 지렁이 수
#import sys
#sys.stdin = open("input.txt", "r")

from collections import deque

# 입력 받기
T = int(input())

for tc in range(1, 1+T):

    # M:가로 N: 세로 배추위치:K
    M, N, K = map(int, input().split())
    # print(M, N, K)
    # 빈 그래프 생성
    graph = [[0]* (M) for _ in range(N)]
    # 방문기록 
    visited = [[0]* (M) for _ in range(N)]
    # print(visited) 

    # 상하좌우 델타배열 지정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] 

    # 빈 그래프에 값 넣기
    for _ in range(K):
        y, x = map(int, input().split())
        # graph[행(세로)][열(가로)] 순서로 적어야 함.
        graph[x][y] = 1    
    # print(graph)

    # 넓이 출력 dfs
    def bfs(start_x, start_y):
        # 큐 생성 및 초기값 지정
        queue = deque([(start_x, start_y)])
        # 시작점 방문 처리
        visited[start_x][start_y] = 1
        # 큐 빌때까지 while 탐색
        while queue :
            #맨 앞에 꺼내서 현재 위치로 삼기
            x, y = queue.popleft()
            #현재 위치를 기준으로 4방향 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 유효한 범위 인지 확인
                if 0 <= nx < N and 0 <= ny < M:
                    if visited[nx][ny] == 0 and graph[nx][ny]==1:
                        #유효한 범위라면 
                        # 1. 방문처치
                        visited[nx][ny] = 1
                        # 다음 탐색을 위해 현재 위치 큐에 저장
                        queue.append((nx, ny))
        # while 끝나면 최종 결과 반환
    cnt = 0
    # 시작점(1인 부분)찾기 루프
    # 1. 좌표 접근
    for i in range(N):
        for j in range(M):
            # 값이 1이고, 방문 안했는지 확인
            if graph[i][j] == 1 and visited[i][j] ==0 :
                # 유효한 조건이라면 탐색기 호출
                # 호출기에 현재 좌표 넘겨주고
                bfs(i, j) 
                # 호출이 끝나면 갯수 추가
                cnt +=1  
    print(cnt)            



