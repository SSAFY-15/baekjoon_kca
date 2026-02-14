N = int(input())
li = [input() for _ in range(N)]
# print(li)
for score in li:
    total =0
    current = 0
    for s in score:
        if s == "O":
            current += 1
            total += current
        else: 
            current = 0
            total += current

    print(total)