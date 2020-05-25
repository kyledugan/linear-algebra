import numpy as np
import sys
sys.path.append('../week5')
sys.path.append('../week3')
from matrix_matrix_mult_columns import matrix_matrix_mult_columns
from matrix_vector_mult import matrix_vector_mult

def gauss_jordan_elimination(A, b):
    if len(A.shape) != 2 or len(b.shape) != 2:
        return "FAILED"
    if A.shape[0] != A.shape[1]:
        return "FAILED"
    if b.shape[0] != A.shape[0] or b.shape[1] != 1:
        return "FAILED"

    for i in range(A.shape[0]):
        # construct pivot matrix
        P = np.identity(A.shape[0])
        for j in range(A.shape[0]):
            if i != j:
                P[j,i] = -A[j,i] / A[i,i]

        # update appended matrix
        A = matrix_matrix_mult_columns(P, A)
        b = matrix_vector_mult(P, b)

    # solve for b
    for i in range(A.shape[0]):
        b[i,0] /= A[i,i]

    return b

A = np.array([[-2,2,-5], [2,-3,7], [-4, 3, -7]])
b = np.array([[-7], [11], [-9]])
print(gauss_jordan_elimination(A, b))