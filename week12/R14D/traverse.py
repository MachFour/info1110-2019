L = (   [1, 2, 3, 4, 5],
        ('a', 'b'),
        [True, False, True],
        [0.0000000000000000001],
        [[]]
        )

def traverse(L):
    i = 0
    if not (isinstance(L, list) or isinstance(L, tuple)):
        raise TypeError("L should be a list")
    while i < len(L):
        ith_list = L[i]
        if not (isinstance(ith_list, list) or isinstance(ith_list, tuple)):
            raise TypeError("item {:d} in L should be a list".format(i))
        j = 0
        while j < len(ith_list):
            print(ith_list[j], end = ' ')
            j += 1
        # move to next line
        print(end="\n") # explicitly show newline
        i += 1
