import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(parent, x):
    #부모를 찾을 때까지 
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(parent, a, b): #두 그룹 합치기 
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a!= root_b:
        parent[root_b] = root_a # 이거 두 개는 바꿔도 돼. 상관 없어. 


n , m = map(int,input().split())

parent = [i for i in range(n+1)] #모두 자기 자신이 부모
cycle_turn = 0 # 사이클 발생 저장 변수 
for i in range(1, m+1): 
    a, b = map(int, input().split())

    #만약 이미 사이클이 있으면?
    if cycle_turn !=0:
        continue

    #선 연결 전, 두 부모가 같은지
    if find(parent, a) == find(parent, b):
        #같으면 사이클 
        cycle_turn = i
    else:
        #다르면 합쳐
        union(parent, a, b)


print(cycle_turn)