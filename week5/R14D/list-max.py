# How to find the maximum item in a list
l = [-1, 1000, 123, 123, 14, 14, 14, 411, 441]

# 'suppose' that the first item is the largest
l_max = l[0] # the value of the largest item
l_max_index = 0 # where it is in the list

i = 0 # iterate through l to see if there are any larger items
while i < len(l):
    # compare current item with largest already seen
    if l[i] > l_max:
        # then l[i] is the largest item seen so far
        l_max = l[i] # save the new largest item
        l_max_index = i # and its position in the list
    i += 1
print("the maximum was {} at index {}".format(l_max, l_max_index))
