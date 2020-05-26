import numpy as np
import sys
sys.path.append('../week5')
from matrix_matrix_mult_columns import matrix_matrix_mult_columns

def gauss_jordan_elimination(A, b):
    if len(A.shape) != 2 or len(b.shape) != 2:
        return "FAILED"
    if A.shape[0] != A.shape[1]:
        return "FAILED"
    if b.shape[0] != A.shape[0]:
        return "FAILED"

    for i in range(A.shape[0]):
        # construct elimination matrix
        P = np.identity(A.shape[0])
        for j in range(A.shape[0]):
            if A[i,i] == 0:
                for k in range(i+1, A.shape[0]):
                    if A[k,i] != 0:
                        # pivot A
                        tmpA = A[i,:].copy()
                        A[i,:] = A[k,:]
                        A[k,:] = tmpA

                        # pivot b
                        tmpB = b[i,:].copy()
                        b[i,:] = b[k,:]
                        b[k,:] = tmpB

                if A[i,i] == 0:
                    return "FAILED - matrix is singular"

            if i != j:
                P[j,i] = -A[j,i] / float(A[i,i])
            else:
                P[j,i] = 1 / float(A[i,i])

        # update appended matrix
        A = matrix_matrix_mult_columns(P, A)
        b = matrix_matrix_mult_columns(P, b)

    return b

# A = np.array([[2,4,-2], [4,8,6], [-2,0,5]])
# b = np.array([[3],[15],[14]])
# print(gauss_jordan_elimination(A, b))