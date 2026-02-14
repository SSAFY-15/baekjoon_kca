A = int(input())
B = int(input())
C = int(input())

result = str(A*B*C)

for i in range(10):#0~9까지
    print(result.count(str(i)))
