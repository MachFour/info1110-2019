import numpy as np

matrix = [  # Length of
    [1, 2],
    [3, 4],
    [5, 6]
] # call this matrix `A`
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
    print()
"""
How could the above loop structure be modified, to print the transpose?
The transpose of the above matrix `A` is:
1 3 5
2 4 6
"""

image = [
            [
                [1,2], # R
                [3,4]
            ],

            [
                [0,255], # G
                [0,5]
            ],

            [
                [3,2], # B 
                [199,1]
            ]

        ]

image_numpy = np.array(image, dtype=np.float64)

for i in range(len(matrix[0])):
    for j in range(len(matrix)):
        print(matrix[j][i], end=' ')
    print()

matrix_n = np.array(matrix, dtype=np.int32)

#print(matrix_n)

#print(matrix_n.T)

#a = np.matmul(matrix_n, matrix_n.T)

#print(matrix_n * matrix_n.T)
