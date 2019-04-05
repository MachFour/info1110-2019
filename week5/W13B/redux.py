def avg(lst_nums):
    i = 0
    sum_lst = 0
    while i < len(lst_nums):
        sum_lst += lst_nums[i]
        i+=1

    avg = sum_lst/len(lst_nums)

    return avg

def redux(num_lst):
    average_num = avg(num_lst)

    diff_lst = []

    i = 0
    while i < len(num_lst):
        diff_lst.append( (i, abs(num_lst[i]-average_num)) )
        i += 1

    return diff_lst

l = [5, 3, 2, 4, 10]

print(redux(l))
