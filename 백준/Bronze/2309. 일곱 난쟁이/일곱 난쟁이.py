
arr =[]
for _ in range(9):
    N = int(input())
    arr.append(N)
# print(arr)
a = True    
arr_sort = sorted(arr)
idx1 =0
idx2 =0
total= sum(arr_sort)
# print(total)
for i in range(0, 9):
    total -= arr_sort[i]
    idx1 = arr_sort[i]
    for j in range(1,9):
        total -= arr_sort[j]
        idx2 = arr_sort[j]

        if total == 100: 
            a = False
            break
           
        total +=arr_sort[j]
    if a == False:    
        break
    total += arr_sort[i]


# print(idx1, idx2)
for i in range(0,9):
    if arr_sort[i] != idx1 and  arr_sort[i] !=  idx2:
        print(arr_sort[i])


        
    