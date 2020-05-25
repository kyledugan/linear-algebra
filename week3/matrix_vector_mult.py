import numpy as np
import sys
sys.path.append('../week1')
from dot import dot

def matrix_vector_mult(A,x):
    res = np.zeros((A.shape[0], 1))
    # check that inputs are 2x2 arrays
    if len(A.shape) != 2 or len(x.shape) != 2:
        return "FAILED"
    # check that x is a column vector
    if x.shape[1] != 1:
        return "FAILED"
    # check that inputs have compatible dimensions
    if A.shape[1] != x.shape[0]:
        return "FAILED"

    for i in range(A.shape[0]):
        res[i,0] = dot(np.array([A[i]]), x)
    
    return res

# A = np.array([[2,0,1],[1,1,0],[2,0,1],[1,1,0]])
# x = np.array([[-1],[1],[1]])
# A = np.array([[2,0,1,2], [-2,-1,1,-1], [4,-1,5,4], [-4,1,-3,-8]])
# x = np.array([[1], [-1], [2], [-1]])
# print(matrix_vector_mult(A,x))
