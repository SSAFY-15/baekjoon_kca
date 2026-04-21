# 백준 1916번 최소비용 구하기
# 다익스트라
import heapq
import sys

#sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


# 입력받는 함수
def solve():
    # N:도시 갯수(노드), M:버스의 개수(간선)   
    n = int(input())
    m = int(input())

    # 인접리스트 
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        # u번 도시에서 v번 도시로 가는 비용이 w임.
        graph[u].append((v, w))

    # 출발도시와 도착도시 번호 입력
    start_node, end_node = map(int, input().split())

    # 다익스트라 초기화
    inf = float('inf')  # 최단거리 테이블을 무한대로 초기화
    distance = [inf]*(n+1)

    #우선 순위 큐 생성
    # 큐에 (비용, 현재_도시)현태로 저장
    # 비용이 낮은 순으로 정렬되게 함
    pq = []

    # 시작점 설정: 자기 자신으로 가는 비용은 0
    distance[start_node] =0
    heapq.heappush(pq, (0, start_node))

    # 다익스트라 시작
    while pq:
        # 현재 가장 짧은 거리에 있는 노드 꺼내기
        dist, now = heapq.heappop(pq)
        #이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    print(distance[end_node])
    
if __name__ == "__main__":
    solve()    
