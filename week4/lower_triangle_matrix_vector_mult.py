import numpy as np
import sys
sys.path.append('../week1')
from dot import dot

def transpose_matrix_vector_mult(A,x,y):
    # check that all inputs are 2x2 arrays
    if len(A.shape) != 2 or len(x.shape) != 2 or len(y.shape) != 2:
        return "FAILED"
    # check that x and y are both column vectors
    if y.shape[1] != 1 or x.shape[1] != 1:
        return "FAILED"
    # check that inputs have compatible dimensions
    if y.shape[0] != x.shape[0] or A.shape[1] != x.shape[0]:
        return "FAILED"

    for i in range(A.shape[1]):
        y[i,0] += dot(np.array([A[i,:i+1]]), x[:i+1])
    
    return y

A = np.array([[1,0,0,0,0], [2,-2,0,0,0], [0,-4,3,0,0], [3,1,-2,1,0], [-1,2,1,-1,-2]])
x = np.array([[-1], [0], [2], [-1], [1]])
y = np.array([[0], [0], [0], [0], [0]])
print(transpose_matrix_vector_mult(A,x,y))