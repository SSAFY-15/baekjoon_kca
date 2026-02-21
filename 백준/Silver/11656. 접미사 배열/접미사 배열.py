
S = input()
# 한 글자씩 떼서 리스트에 담기
word_list = list(S)   # ['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']
# print(word_list)

# 접미사들 저장할 빈 리스트
sort_word = []
# 뒤에서 부터 +1 글자씩 가져옴
# ex. i = 1 ['n'], i=2 ['o', 'n']
for i in range(1, len(word_list)+1):
    word = word_list[-i:]
    # 떼어낸 리스트들을 공백없이 문자열로 저장. ['o', 'n'] -> on
    sort_word.append("".join(word))
# 사전순으로 정렬
sort_word.sort()
# print(sort_word)

#정렬된 단어 하나씩 꺼내기
for s in sort_word:
    print(s)
    



