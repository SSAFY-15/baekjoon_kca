N , M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
result = [[0] * M for _ in range(N)]
# print(result)
for i in range(N):# 행 반복
    for j in range(M): # 열 반복
        result[i][j] = arr[i][j] + arr2[i][j]

for row in result:
    print(*row) 