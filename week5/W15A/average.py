def average(lst):
    sum_lst = 0
    i = 0
    while i < len(lst):
        sum_lst += lst[i]
        i+=1

    average_val = sum_lst/len(lst)

    diff_lst = []

    i = 0
    while i < len(lst):
        diff_lst.append(abs(lst[i]-average_val))
        i+=1

    i = 0
    max_val = diff_lst[0]
    max_index = 0

    while i < len(diff_lst):
        if max_val < diff_lst[i]:
            max_val = diff_lst[i]
            max_index = i
        i +=1

    return max_index, max_val


ls = [5, 3, 2, 4, 10]

print(average(ls))
