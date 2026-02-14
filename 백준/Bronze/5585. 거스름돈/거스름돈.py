cost = int(input())
# 거스름돈 계산
result = 1000 - cost
coins = [500, 100, 50, 10, 5, 1]
total = 0
for coin in coins:
    total += result // coin 
    result = result % coin

    if result == 0:
        break

print(total)   