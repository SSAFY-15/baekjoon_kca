import sys

sys.setrecursionlimit(10**6) # 재귀 깊이 제한 늘리기
input = sys.stdin.readline # 데이터 한 줄씩 빠르게 읽어오기

# 루트 찾는 함수
def find(parents, x): # x노드가 속한 집합의 루트를 탖기
    if x == parents[x]:
        return x  
    # 자신이 루트가 아니라면, 합치기
    parents[x] = find(parents, parents[x])
    return parents[x]

# 두 노드를 하나로 합치는 함수 => 각 그룹의 루트끼리 합치는
def union(parents, y, x):
    rep_y = find(parents, y)
    rep_x = find(parents, x)
    # 여기서 루트가 같으면 
    if rep_y == rep_x:
        return False
    
    if rep_y < rep_x:
        parents[rep_x] = rep_y
    else:
        parents[rep_y] = rep_x
    return True
# 데이터 불러와서 그래프 연결
def solve():
    line = input().split()
    if not line: return
    
    V, E = map(int, line)
    
    edges = []
    for _ in range(E):
        u, v, weight = map(int, input().split())
        edges.append((weight, u, v))
    
    edges.sort()
    
    parents = [i for i in range(V + 1)]
    total_weight = 0
    edges_count = 0
    
    for weight, u, v in edges:
        if union(parents, u, v):
            total_weight += weight
            edges_count += 1
            
            if edges_count == V - 1:
                break
                
    print(total_weight)


solve()
