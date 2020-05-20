import numpy as np
import sys
sys.path.append('../week3')
from matrix_vector_mult import matrix_vector_mult

def matrix_matrix_mult_columns(A,B,C):
    if len(A.shape) != 2 or len(B.shape) != 2 or len(C.shape) != 2:
        return "FAILED"
    if A.shape[1] != B.shape[0] or A.shape[0] != C.shape[0] or B.shape[1] != C.shape[1]:
        return "FAILED"
    for i in range(B.shape[1]):
        C[:,[i]] += matrix_vector_mult(A, np.array(B[:,[i]]), np.array(C[:,[i]]))
    return C

A = np.array([[-2,1,2],[3,2,1],[-1,0,-3]])
B = np.array([[-1,-2,3], [0,1,2], [-3,2,1]])
C = np.array([[0,0,0], [0,0,0], [0,0,0]])
print(matrix_matrix_mult_columns(A,B,C))