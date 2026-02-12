# 입력
N, M = map(int,input().split())

def recur(cnt, path):
    #2.끝(종료조건)
    # M개 만큼 숫자를 고른 상태 라면
    if cnt == M:
        print(*path, sep=' ') #최종 태스크: 현재의 path 리스트 출력
        return
    
    # 3.반복할 기능 설정
    # 1부터 N까지 숫자 뽑아서 path에 넣기
    for i in range(1, N+1):
        path.append(i)
    # 4.다음 함수에 넘겨줄 값 지정    
        recur(cnt+1, path)
    #5.(문제 마다 다름) 함수가 끝나고 다음 진행을 위해 해야할 작업 설정
    # i=2의 조합을 봐야하기 때문에 맨 뒤에 숫지 제거
        path.pop()
        


# 1. 시작상황 설정, 시작에서 넘겨줄 값 지정
# 숫자를 0개 고르고, 리스트가 빈 상태)
recur(0, [])