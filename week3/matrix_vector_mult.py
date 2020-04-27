import numpy as np
import sys
sys.path.append('../week1')
from dot import dot
from transpose import transpose

def matrix_vector_mult(A,x,y):
    # check that all inputs are 2x2 arrays
    if len(A.shape) != 2 or len(x.shape) != 2 or len(y.shape) != 2:
        return "FAILED"
    # check that x and y are both column vectors
    if y.shape[1] != 1 or x.shape[1] != 1:
        return "FAILED"
    # check that inputs have compatible dimensions
    if y.shape[0] != x.shape[0] or A.shape[1] != x.shape[0]:
        return "FAILED"

    for i in range(A.shape[0]):
        y[i,0] += dot(np.array([A[i]]), transpose(x))
    
    return y

A = np.array([[-1, 0, 2], [2, -1, 1], [3, 1, -1]])
x = np.array([[-1], [2], [1]])
y = np.array([[1], [1], [1]])
print(matrix_vector_mult(A,x,y))
