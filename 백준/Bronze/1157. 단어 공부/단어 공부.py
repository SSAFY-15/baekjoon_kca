str = input().upper()
cnt_list = []  #갯수 저장할 빈 리스트
str_set = list(set(str))
# print(str_set) : ['M', 'I', 'S', 'P']

#str_set에서 한 알파벳씩 꺼내서 비교
for s in str_set:
    # 원본인str에서 꺼낸 알파벳(s)가 몇개 있는 지 카운트
    count = str.count(s)
    # 갯수 저정하는 리스트에 카운트 저장
    cnt_list.append(count)
    # print(cnt_list) : [4, 4, 1, 1]
if cnt_list.count(max(cnt_list)) >= 2:
    print("?")
else:
    max_cnt = max(cnt_list) # 4
    max_idx = cnt_list.index(max_cnt) # 1
    # print(max_idx)
    print(str_set[max_idx])
      