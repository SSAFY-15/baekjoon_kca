N = int(input())
cards = set(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))
# print(N, M)
# print(cards, nums)
# nums 의 숫자들을 하나씩 빈 리스트에 담기
nums_idx = [0] * len(nums)
# for num in nums:
#     nums_idx.append(num)
# print(nums_idx)

for i in range(M):
    # cards의 i번째 숫자가 nums에 있다면 
    if nums[i] in cards:
        nums_idx[i] += 1
print(*nums_idx)