import numpy as np
import sys
sys.path.append('../week3')
from matrix_vector_mult import matrix_vector_mult

def matrix_matrix_mult_columns(A,B):
    res = np.zeros((A.shape[0], B.shape[1]))
    if len(A.shape) != 2 or len(B.shape) != 2:
        return "FAILED"
    if A.shape[1] != B.shape[0]:
        return "FAILED"
    for i in range(B.shape[1]):
        res[:,[i]] = matrix_vector_mult(A, np.array(B[:,[i]]))

    return res

# A = np.array([[1,0,1],[0,1,-2],[0,0,1]])
# B = np.array([[-2,0,-1,1],[0,-1,2,4],[0,0,1,1]])
# print(matrix_matrix_mult_columns(A,B))