# a 3 dimensional list:
list_3d = [ [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ], [
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15]
        ], [
            [17, 18, 19],
            [20, 21, 22],
            [23, 24, 25]
        ] ]

list_4d = [list_3d, list_3d, list_3d]

# lazy way to index if you assume all lists are the same length
i = 0
#for i in range(len(list_3d)):
while i < len(list_3d):
    for j in range(len(list_3d[0])):
        for k in range(len(list_3d[0][0])):
            print(list_3d[i][j][k], end = " ")
        print()
    print()
    i += 1
print()
