import numpy as np
from gaussian_elimination import gaussian_elimination


# takes a square matrix A and returns square matrices L and U such that LU = A
def lu_factorization(A):
    if len(A.shape) != 2:
        return "FAILED"
    if A.shape[0] != A.shape[1]:
        return "FAILED"

    A = gaussian_elimination(A)
    L = np.zeros((A.shape[0], A.shape[1]))
    U = np.zeros((A.shape[0], A.shape[1]))
    for i in range(A.shape[0]):
        tmp = np.concatenate((A[i, :i], np.array([1])))
        L[i] = np.concatenate((tmp, np.zeros(A.shape[0] - i - 1)))
        U[i] = np.concatenate((np.zeros(i), A[i, i:]))
    return L, U

# A = np.array([[1,-2,2], [5,-15,8], [-2,-11,-11]])
A = np.array([[2,0,1,2], [-2,-1,1,-1], [4,-1,5,4], [-4,1,-3,-8]])
L, U = lu_factorization(A)
print(L)
print(U)