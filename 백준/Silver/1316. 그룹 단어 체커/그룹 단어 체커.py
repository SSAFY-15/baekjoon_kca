N = int(input())
li = [input() for _ in range(N)]
# N(단어 갯수) 에서 빼는 방식
cnt = N
for word in li:
    #단어들의 한 글자씩
    for i in range(len(word)-1):
        
        if word[i] != word[i+1]: # 앞 뒤 글자가 다르면
            if word[i] in word[i+1:]:
                cnt -= 1
                break
                
print(cnt) 
