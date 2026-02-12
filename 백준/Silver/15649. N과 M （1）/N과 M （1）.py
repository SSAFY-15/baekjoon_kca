#입력
N, M = map(int, input().split())
used = [0]*(N+1)
def recur(cnt, path):
    # 끝점 설정
    if cnt == M:
        #최종 결과물
        print(*path, sep=' ')
        return
    #반복 작업 설정
    for i in range(1, N + 1):
        # 중복확인 조건 추가
        if used[i] == 1:
            continue # 다음 i로
        #중복이 아니라면, 숫자 추가하고
        path.append(i)
        # 사용기록 남기기
        used[i] = 1
        #다음 재귀에 넘겨줄 값 지정
        recur(cnt+1, path)
        #종료조건에 의해 재귀가 끝났을때, 다음 작업을 위한 조건설정
        path.pop()# 다음 조합을 알아보기 위해 맨 뒤 숫자 제거
        used[i]=0 #사용기록 초기화

    
# 시작점 설정
recur(0, [])