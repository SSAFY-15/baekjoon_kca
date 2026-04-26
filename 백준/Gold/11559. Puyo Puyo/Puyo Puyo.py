"""
puyo puyo 문제 / 백준 11559번

- 너비 우선 탐색(BFS)
- 중력 메커니즘- 바닥이 없으면 떨어지는 

1. 상하좌우로 인접한 색깔 뿌요가 4개 이상인 그룹을 찾기
 => 이떄, visited 로 중복 탐색 방지. 터뜨려야 할 좌표들을 리스트에 따로 보관
 
2. 1에서 찾은 좌표값들의 값을 . 으로 바꾸기
 => 모든 칸의 검사가 마친 후에 한꺼번에 터뜨려야 함.
   왜냐? 이 문제를 중력 메커니즘이 있음. 
         하나 터진 후에 바로 중력을 적용하면, 같은 타이밍에 터져야 할 다른 뿌요들이 인식을 못함.

3. 리스트 재구성하기
 => 각 열을 순회하며 빈칸(.)이 아닌 뿌요데이터(문자열)만 순서대로 추출
  전체 높이에서 추출한 뿌요 갯수를 뺌, 그 차이 만큼 빈칸(.)을 리스트 앞부분에 추가함
  ex)
    ['.', 'G', '.', '.', 'B', '.', 'R', '.', '.', '.', '.', '.']
    문자만 추출: ['G', 'B', 'R'] =>3개
    앞부분 채우기: 빈칸(.)을 (12-3)개 준비
    빈칸 추가: ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'G', 'B', 'R']

"""

import sys
#sys.stdin = open("input.txt", "r")
from collections import deque

# 초기 맵 설정
graph = [list(sys.stdin.readline().strip()) for _ in range(12)] # 맵 크기가 12x6으로 정해져 있움

# 방향 벡터 설정
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# bfs 함수 정의
# 같은 색깔로 연결된 뿌요들을 찾고, 4개 이상이면 해당 좌표를 반환하는 함수
def bfs(r, c, color):
    queue = deque([(r, c)]) # 시작 좌표를 큐에 넣기
    visited[r][c] = True  # 시작지점 방문처리
    group = [(r, c)] # 현재 탐색에서 찾은 같은 색깔 부요들이 좌표를 모아둘 리스트

    # 큐 빌 때까지 반복
    while queue:
        curr_r, curr_c = queue.popleft() # 가장 앞에 있는 좌표 꺼내서 현재 위치로 지정
        # 상하좌우 탐색
        for i in range(4):
            nr, nc = curr_r + dr[i], curr_c + dc[i] # 현재 위치에서 4방향 확인해서 다음 좌표 계산(nr, nc)
            # 다음 좌표가 유효한 방향인지 쳌,
            if 0 <= nr < 12 and 0 <= nc < 6 : # 다음 좌표가 맵(12x6)을 벗어나는지 확인

                # 아직 방문하지 않은 칸이고, 시작점과 색깔이 같다면
                if not visited[nr][nc] and graph[nr][nc] == color:                      
                    visited[nr][nc] = True # 해당 좌표 방문처리
                    queue.append((nr, nc)) # 해당 좌표 큐에 넣어서 다음 시작점로 지정
                    group.append((nr, nc)) # 해당 좌표 그룹에 넣어서 터트릴 후보에 올림

    # bfs 탐색이 끝난 후, 쌓인 group의 길이가 4이상이면 좌표 리스트를 반환.
    # 4 미만이면 빈 리스트 반환
    return group if len(group) >= 4 else []   
    

# 중력 메커니즘 적용
# 빈공간(.)을 앞으로, 유효 데이터를 뒤로 정렬하는 함수
def gravity():

    # 현재 열에서 실제 뿌요 데이터만 추출
    for c in range(6):  #열에서 왼 -> 오 하나씩 확인       
        puyos=[]  # 해당 열에 문자열(뿌요데이터)만 임시로 담아둘 빈 리스트 생성
       
        for r in range(12):   # 해당 열을 위에 아래로 돌면서 
            if graph[r][c] != '.':  # .이 아닌 데이터만
                puyos.append(graph[r][c]) # puyos 리스트에 추가

        # 새로운 열 데이터 구성: (전체 높이 - 뿌요 개수)만큼 앞에 빈 공간을 채움
        # 1. 12칸 중에서 puyo가 들어갈 자리를 제외한 나머지 빈칸 수 만큼 .을 만들고
        # 2. 위에서 뽑아둔 puyos 리스트에 이어 붙이기
        new_col = ['.'] * (12-len(puyos)) + puyos

        # 원본 맵에 반영
        # 새로 구성된 new_col을 원래 맵 데이터의 해당 열에 위에서 부터 덮어씌우기
        for r in range(12):
            graph[r][c] = new_col[r]  

# 연쇄 카운팅
total_chains = 0
# 터질게 없을 때까지 반복
while True:
    is_popped = False  # 현재 턴에 한 번이라도 뿌요가 터졌는지 기록/ 매 턴마다 False로 초기화
    visited = [[False] * 6 for _ in range(12)] # 매 턴마다 방문기록 초기화. 
                                               # 왜냐? 다음턴에 맵 전체를 다시 온전하게 탐색하기 위해


    # 맵 전체를 훑으며 터뜨릴 그룹 찾기
    for r in range(12):
        for c in range(6):
            # 빈칸이 아니면서 아직 방문하지 않은 부요를 발견하면
            if graph[r][c] != '.' and not visited[r][c]:
                # bfs 탐색 시작. 
                # bfs 결과를 bomb_list에 담음
                bomb_list = bfs(r, c , graph[r][c])
                
                # 만약 bomb_list에 터트릴 좌표가 있다면
                if bomb_list:
                    is_popped = True # True로 설정
                    for br, bc in bomb_list:
                        graph[br][bc] = '.'  #그리고 해당 좌표를 .으로 변경 => 맵에서 지우는거


    # 더 이상 터질 뿌요가 없다면 종료
    if not is_popped:
        break
    # 터진 부분들은 def gravity()을 적용해서 빈칸 채움
    gravity()
    total_chains += 1  # 무사히 한 턴이 끝나면 +1
                       # 무사히 한 턴: 폭파 + 중력

print(total_chains)





        

                


    