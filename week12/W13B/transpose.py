import numpy as np

matrix = [  # Length of
    [1, 2],
    [3, 4],
] # call this matrix `A`
#for i in range(len(matrix)):
#    for j in range(len(matrix[0])):
#        print(matrix[i][j], end=' ')
#    print()
"""
How could the above loop structure be modified, to print the transpose?
The transpose of the above matrix `A` is:
1 3 5
2 4 6
"""


#for i in range(len(matrix[0])):
#    for j in range(len(matrix)):
#        print(matrix[j][i], end=' ')
#    print()

matrix_n = np.array(matrix, dtype=np.int32)

print(matrix_n)

print(matrix_n.T)

a = np.matmul(matrix_n, matrix_n.T)

print(matrix_n * matrix_n.T)
