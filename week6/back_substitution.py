import numpy as np
from gaussian_elimination import gaussian_elimination

def back_substitution(A, b):
    if len(A.shape) != 2 or len(b.shape) != 2:
        return "FAILED"
    if A.shape[0] != A.shape[1]:
        return "FAILED"
    if b.shape[0] != A.shape[0] or b.shape[1] != 1:
        return "FAILED"
    
    for i in range(A.shape[0]):
        b[i+1:,0] -= b[i,0] * A[i+1:,i]

    for i in range(A.shape[0]-1, -1, -1):
        div = b[i,0]
        for j in range(i+1, A.shape[0]):
            div -= A[i,j] * b[j,0]
        b[i,0] = div / A[i,i]
    return b

b = np.array([[2],[2],[11],[-3]])
A = gaussian_elimination(np.array([[2,0,1,2], [-2,-1,1,-1], [4,-1,5,4], [-4,1,-3,-8]]))
# A = gaussian_elimination(np.array([[-1,2,-3], [-2,2,-8], [2,-6,6]])
# b = np.array([[2], [10], [-2]])
# print(back_substitution(A, b))