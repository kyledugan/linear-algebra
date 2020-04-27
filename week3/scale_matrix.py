import numpy as np

def scale_matrix(A, b):
    if len(A.shape) != 2:
        return "FAILED"
    
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A[i,j] *= b

    return A

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(scale_matrix(A, 3))