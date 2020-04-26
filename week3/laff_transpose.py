import numpy as np

def laff_transpose(A):
    # check for 2x2 array
    if len(A.shape) != 2:
        return "FAILED"

    B = np.zeros((A.shape[1], A.shape[0]), dtype=int)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            B[j][i] = A[i][j]

    return B

A = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(laff_transpose(A))