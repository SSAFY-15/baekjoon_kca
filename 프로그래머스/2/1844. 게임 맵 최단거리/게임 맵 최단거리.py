from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    # 4방향 벡터
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 큐에 현재 좌표, 거리 넣기
    queue = deque([(0, 0, 1)])
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    # 큐 빌 때까지 반복
    while queue:
        r, c, dist = queue.popleft()

        # 목적지에 도달하면 거리 반환
        if r == n-1 and c == m-1:
            return dist

        # 상하좌우 탐색
        for i in range(4):
            nr, nc = r +dr[i], c+dc[i]
            # 유효한 범위인지 탐색
            if 0 <= nr < n and 0 <= nc <m and maps[nr][nc] == 1:
                # 아직 방문하지 않았는지 확인
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    # 다음을 위해서 현재 칸을 큐에 넣기
                    queue.append((nr, nc, dist +1))
    return -1

