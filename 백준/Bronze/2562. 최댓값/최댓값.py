numbers = [int(input()) for _ in range(9)]
# print(numbers)
max_val=0
max_idx=numbers[0]
for i in range(9):
    if numbers[i] > max_val:
        max_val = numbers[i]
        max_idx = i+1
print(max_val, max_idx)    
