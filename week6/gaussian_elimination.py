import numpy as np

# A must be an n x (n+1) matrix / augmented matrix
def gaussian_elimination(A):
    if len(A.shape) != 2:
        return "FAILED"
    if A.shape[0] != A.shape[1]:
        return "FAILED"
    
    for i in range(A.shape[0]-1):
        A[i+1:,i] /= A[i,i]
        for j in range(i+1, A.shape[0]):
            for k in range(i+1, A.shape[0]):
                A[j][k] -= A[j][i] * A[i][k]
    return A

A = np.array([[2,0,1,2], [-2,-1,1,-1], [4,-1,5,4], [-4,1,-3,-8]])
# print(gaussian_elimination(A))