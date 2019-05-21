import numpy as np

# 'matrix' (list of lists) in python
A = [
        [1, 2],
        [3, 4],
        [5, 6]
]

print("A = ")
print()
for i in range(3):
    for j in range(2):
        print(A[i][j], end=' ')
    print()
print()
print()

# transpose

print("A^T = ")
print()

for j in range(2):
    for i in range(3):
        print(A[i][j], end=' ')
    print()

print()


# matrix multiplication with numpy
B = np.array([
    [1,1],
    [0,1]
    ])
C = np.array([
    [2,0],
    [3,4]
    ])

D = B @ C
print("B = ", end="\n\n")
print(B, end="\n\n")
print("C = ", end="\n\n")
print(C, end="\n\n")
print("D = ", end="\n\n")
print(D, end="\n\n")
