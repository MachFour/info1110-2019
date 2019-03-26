# swaps the first two items in l
# This works because the list l is
# passed by *reference*
def swap_list(l):
    if len(l) < 2:
        pass
    else:
        # swap
        tmp = l[0]
        l[0] = l[1]
        l[1] = tmp

# now test it
l = [3, 4]
print("Before swap: l is", l)
swap_list(l)
print("After swap: l is", l)
