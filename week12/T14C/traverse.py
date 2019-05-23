
def traverse(ls):
    #if type(ls) != list:
    if not isinstance(ls, list):
        raise TypeError("The argument must be a list.")
    # iterate over the first items
    i = 0
    while i < len(ls):
        inner_list = ls[i]
        if not isinstance(inner_list, list):
            raise TypeError("The item at index {:d} is not a list".format(i))
        # now we know it's a list
        j = 0
        while j < len(inner_list):
            # print out everything on one line
            print(inner_list[j], end = " ")
            j += 1
        print() # end the line
        #print(inner_list)
        i += 1

# this is not useful!
# print(traverse(L)) # prints None



# example lists:
L = [
        [1, 2, 3, 4],
        ["a", "b", "c"],
        [True, False]
    ]

M = [
        [4, 1, 2, 3, 4],
        ["c"],
        []
    ]

traverse(L)
print()
traverse(M)
