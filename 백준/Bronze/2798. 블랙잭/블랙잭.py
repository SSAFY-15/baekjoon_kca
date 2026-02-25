N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# print(numbers)

total = 0
max_total = 0

def recur(cnt, idx):
    global total
    global max_total

    # 종료조건: 카드를 3장 뽑았을떄
    if cnt == 3 :
        # 그 카드들의 합이 21 이하일때, 최댓갑을 갱신
        if M >= total:
            max_total = max(max_total, total)

        # if M >= total > max_total:
        #     max_total = total

        return
    
    # 이미 기준값을 넘겼을 경우
    if total > M:
        return

    # 반복할 동작
    for i in range(idx, N):
        total += numbers[i]

        recur(cnt+1, i+1)
        # 종료조건을 만나서 다음턴으로 갈 작업
        total -= numbers[i]   


# 초기 입력값
recur(0, 0)

print(max_total)