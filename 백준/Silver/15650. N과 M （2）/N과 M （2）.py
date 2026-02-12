# + 오름차순..

#입력
N, M = map(int, input().split())
used = [0]*(N+1)
def recur(cnt, path, start):
    # 끝점 설정
    if cnt == M:
        #최종 결과물
        print(*path, sep=' ')
        return
    #반복 작업 설정
    i = 1
    for i in range(start, N + 1):
        # 중복확인 조건 추가
        if used[i] == 1:
            continue # 다음 i로
        
        #오름차순 설정
        # 만약 1번째로 뽑힌 숫자가 현재 뽑힌 숫자보다 크다면 다음으로 넘기기
      
        #중복이 아니라면, 숫자 추가하고
        path.append(i)
        # 사용기록 남기기
        used[i] = 1
        #다음 재귀에 넘겨줄 값 지정
        # 오름차순:다음 숫자는 지금의 i보다 1 큰 숫자부터시작
        recur(cnt+1, path, i+1)
        #종료조건에 의해 재귀가 끝났을때, 다음 작업을 위한 조건설정
        path.pop()# 다음 조합을 알아보기 위해 맨 뒤 숫자 제거
        used[i]=0 #사용기록 초기화

    
# 시작점 설정
recur(0, [], 1)