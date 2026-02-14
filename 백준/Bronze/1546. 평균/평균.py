N = int(input())
scores = list(map(int, input().split()))
# print(scores)
max_num = max(scores)

new_score = []
for score in scores:
    result = (score / max_num) * 100
    new_score.append(result)

new_mean = sum(new_score) / len(new_score)
print(new_mean)   
    