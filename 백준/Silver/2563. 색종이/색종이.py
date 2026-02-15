N = int(input()) 
# 100 x 100 도화지
graph = [[0]* 100 for _ in range(100)] 
#검은색 색종이
cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    # 10 x 10 종이여서 +10
    for i in range(x, x+ 10):
        for j in range(y, y+10):
            # 겹쳐지는 부분 고려
            # 아직 안 채워져있는(0)아라면 1로 채우고
            # + 1 : 넓이
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
print(cnt)      