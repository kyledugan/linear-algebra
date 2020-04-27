import numpy as np

def diagonal(A,x):
    # check for 2D matrix
    if len(A.shape) != 2 or len(x.shape) != 2:
        return "FAILED"
    # check that A is n x n matrix and x is a column vector
    if A.shape[0] != A.shape[1] or x.shape[1] != 1:
        return "FAILED"
    
    for i in range(A.shape[0]):
        for j in range(A.shape[0]):
            if i == j:
                A[i][j] = x[i][0]
            else:
                A[i][j] = 0
    
    return A

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
x = np.array([[10],[11],[12]])
print(diagonal(A,x))