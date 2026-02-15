T = int(input())
# result = []
for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = [] # 한 줄 씩 입력받을때마다 result초기화
    for s in S:
        result.append(s*R)   

    print(*result, sep='')