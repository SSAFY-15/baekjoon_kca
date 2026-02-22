import sys
sys.setrecursionlimit(10**6)
#sys.stdin = open("input.txt", "r")
# 약수 확인해서 저장하는 함수
def recur(num, acc_list):
    # 종료조건
    if num > N//2 : # 현재 숫자가 N//2보다 크면 종료
        return acc_list # 함수 종료하고 지금까지 저장된 약수 리스트를 반환
    if N % num == 0:
        acc_list.append(num)
    return recur(num+1, acc_list)



# 숫자 입력 받기
while True:
    # N을 계속 입력 받다가, -1를 받으면 입력 종료
    N = int(input())
    if N == -1:
        break 
    #함수 호출 시작점
    # 시작 숫자와 빈 리스트 넘기기
    # 최종 재귀 결과를 result에 저장
    result = recur(1, [])

    # 최종결과로 완전수인지 확인
    if sum(result) == N:
        print(f'{N} = {" + ".join(map(str, result))}')
    # 아니라면 문구 출력
    else:
        print(f'{N} is NOT perfect.')